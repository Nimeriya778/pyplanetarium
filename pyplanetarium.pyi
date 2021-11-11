from typing import Tuple

# Type aliases for Rust library types
Point = Tuple[float, float]
Vector = Tuple[float, float]

class SpotShape:
    def __init__(self) -> None: ...
    def scale(self, k: float) -> SpotShape: ...

# Token class
class SpotId:
    pass

class ImageFormat:
    PngGamma8Bpp: ImageFormat = ...
    PngLinear16Bpp: ImageFormat = ...

class Canvas:
    @staticmethod
    def new(width: int, height: int) -> Canvas: ...
    def add_spot(
        self, position: Point, shape: SpotShape, intensity: float
    ) -> SpotId: ...
    def set_spot_offset(self, spot: SpotId, offset: Vector) -> None: ...
    def set_spot_illumination(self, spot: SpotId, illumination: float) -> None: ...
    def clear(self) -> None: ...
    def draw(self) -> None: ...
    def dimensions(self) -> Tuple[int, int]: ...
    def set_background(self, level: int) -> None: ...
    def set_brightness(self, brightness: float) -> None: ...
    def export_image(self, format: ImageFormat) -> bytes: ...