from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sections.tech_effect import TechEffect, EffectCommand


class GameTechEffect(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs): ...

    @abstractmethod
    def make_command(self) -> EffectCommand: ...

    def add_self(self, tech_effects: TechEffect):
        tech_effects.effects.append(self.make_command())
