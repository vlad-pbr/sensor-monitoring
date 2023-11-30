from typing import NamedTuple, Self


class Range(NamedTuple):
    min: int
    max: int

    @classmethod
    def validate_valid_range(cls, _range: Self) -> Self:
        assert _range.min < _range.max, f"minimum value '{_range.min}' is lower than maximum value '{_range.max}'"
        return _range
