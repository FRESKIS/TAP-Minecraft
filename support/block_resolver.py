import mcpi.block as block

def resolve_block_id(name: str) -> int:
    try:
        return getattr(block, name).id
    except AttributeError as e:
        raise ValueError(f"Bloque '{name}' no existe") from e
