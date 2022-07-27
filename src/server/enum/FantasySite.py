from __future__ import annotations

from enum import unique, Enum, auto


@unique
class FantasySite(Enum):
    """
    Used to hold the different types of fantasy football sites.
    """
    ESPN = auto()
    SLEEPER = auto()
    YAHOO = auto()

    @classmethod
    def from_str(cls, s: str) -> FantasySite:
        if s.upper() == "ESPN":
            return FantasySite.ESPN
        elif s.upper() == "SLEEPER":
            return FantasySite.SLEEPER
        elif s.upper() == "YAHOO":
            return FantasySite.YAHOO
        else:
            raise ValueError(f"Unknown value for FantasySite '{s}'.")
