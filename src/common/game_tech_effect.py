from abc import ABC, abstractmethod

from sections.tech_effect import TechEffect, EffectCommand


class GameTechEffect(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs): ...

    @abstractmethod
    def make_command(self) -> EffectCommand: ...

    def add_self(self, tech_effects: TechEffect):
        tech_effects.effects.append(self.make_command())
