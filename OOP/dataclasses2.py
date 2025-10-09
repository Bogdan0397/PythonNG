from dataclasses import dataclass, field

@dataclass
class V3D:
    current_id = 0
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    length: float = field(init=False, compare=False)

    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z)**0.5


