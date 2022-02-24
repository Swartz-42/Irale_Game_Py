from dataclasses import dataclass

@dataclass
class Portal:
    from_world: str
    origin_point: str
    to_world: str
    tp_point: str