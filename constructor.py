import json
from pathlib import Path
from support.block_resolver import resolve_block_id


class constructor:

    def load(self, json_path: str) -> dict:
        js_path = Path("buildings") / f"{json_path}.json"
        return json.loads(Path(js_path).read_text(encoding="utf-8")) 

    def get_requirements(self, json_path: str) -> dict[str, int]:
        data = self.load(json_path)
        requirement: dict = {"Nblocks": data.get("Nblocks", {}), "materials": data.get("materials", {})}

        if not isinstance(requirement, dict):
            raise ValueError("'materials' debe ser un objeto/dict en el JSON")
        return requirement
    def build(self, mc, pos, json_path: str | Path):
        data = self.load(json_path)

        legend_ids = {
            sym: resolve_block_id(block_name)
            for sym, block_name in data["legend"].items()
        }

        for y, layer in enumerate(data["structure"]):
            for x, row in enumerate(layer):
                for z, sym in enumerate(row):
                    mc.setBlock(pos.x + x, pos.y + y, pos.z + z, legend_ids[sym])