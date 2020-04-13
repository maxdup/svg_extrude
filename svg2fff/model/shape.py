import logging
from dataclasses import dataclass, field
from typing import Iterable, Tuple

from svg2fff.model import Polygon, Point, Color
from svg2fff.util import filter_repetition
from svg2fff.css import extract_value

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Shape:
    name: str
    color: Color
    polygon: Polygon

    @classmethod
    def from_svg_path(cls, svg_path, precision: float) -> "Shape":
        fill_rule = extract_value(svg_path.style, "fill-rule")
        if not (fill_rule is None or fill_rule == "evenodd"):
            logger.warning("%s: fill rule %s not supported. Using evenodd instead.", svg_path.id, fill_rule)

        stroke = extract_value(svg_path.style, "stroke")
        if not (stroke is None or stroke == "none"):
            logger.warning("%s: stroked paths are not supported. Ignoring stroke.", svg_path.id)

        fill = extract_value(svg_path.style, "fill")
        if fill:
            fill = Color.from_html(fill, None)

        # 1 px is 1/96 inch; we use mm
        # TODO use m, but we need to convert it to mm when writing the SCAD file.
        px = 25.4 / 96

        def path(segment) -> Tuple[Point]:
            return tuple(Point(p.x*px, p.y*px) for p in filter_repetition(segment))
        segments = svg_path.segments(precision)
        paths = (path(segment) for segment in segments)
        polygon = Polygon(tuple(paths))

        return Shape(svg_path.id, fill, polygon)
