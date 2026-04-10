from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hit {target} make him loose {power} HP"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def spell_combiner(spell1: Callable[[str, int], str], spell2: Callable) -> Callable[[str], Callable[[str, int], str]]:
    
    return map(lambda: spell1, spell1, spell2)

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    ret :Callable = base_spell * multiplier

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    pass

def spell_sequence(spells: list[Callable]) -> Callable:
    pass
