import json
import re
from datetime import datetime, timezone

class JSONMessageHandler:
    _ISO_8601_UTC_Z = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
    _ALLOWED_STATUS = {"SUCCESS", "ERROR", "PENDING"}

    @staticmethod
    def _now_utc_z() -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    @staticmethod
    def _validate(msg: dict):
        required = ["type", "source", "target", "timestamp", "payload", "status"]
        for k in required:
            if k not in msg:
                raise ValueError(f"Missing field: {k}")

        if not isinstance(msg["type"], str) or "." not in msg["type"]:
            raise ValueError("type must be like 'xxxx.vy'")

        if not isinstance(msg["source"], str) or not msg["source"]:
            raise ValueError("source must be a non-empty string")

        if not isinstance(msg["target"], str) or not msg["target"]:
            raise ValueError("target must be a non-empty string")

        ts = msg["timestamp"]
        if not isinstance(ts, str) or not JSONMessageHandler.ISO_8601_UTC_Z.match(ts):
            raise ValueError("timestamp must be ISO8601 UTC: YYYY-MM-DDTHH:MM:SSZ")

        # valida que la fecha exista (no 2025-99-99...)
        datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

        if not isinstance(msg["payload"], dict):
            raise ValueError("payload must be a dict/object")

        if msg["status"] not in JSONMessageHandler.ALLOWED_STATUS:
            raise ValueError(f"status must be one of {JSONMessageHandler.ALLOWED_STATUS}")

        if "context" in msg and msg["context"] is not None and not isinstance(msg["context"], dict):
            raise ValueError("context must be a dict if present")

    @staticmethod
    def to_json(msg_type: str, source: str, target: str, payload: dict,
                status: str = "SUCCESS", context: dict | None = None,
                timestamp: str | None = None) -> str:
        msg = {
            "type": msg_type,
            "source": source,
            "target": target,
            "timestamp": timestamp or JSONMessageHandler.now_utc_z(),
            "payload": payload,
            "status": status,
        }
        if context is not None:
            msg["context"] = context

        JSONMessageHandler.validate(msg)
        return json.dumps(msg)

    @staticmethod
    def from_json(json_str: str) -> dict:
        msg = json.loads(json_str)
        JSONMessageHandler.validate(msg)
        return msg
