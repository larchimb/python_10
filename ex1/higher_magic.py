from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hit {target} make him loose {power} HP"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str,int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined

def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier

def conditional_caster(condition: Callable,
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> str:
        if not condition(target, power):
            return "Spell fizzled"
        else:
            return spell(target, power)
    return conditional

def spell_sequence(spells: list[Callable]
                   ) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence


def condition(target: str, power: int) -> bool:
    if len(target) < 3 or power <= 0:
        return False
    return True

def main() -> None:
    test_values = [20, 5, 18]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("\nTesting spell combiner...")
    combined = spell_combiner(heal, fireball)
    print(*combined(test_targets[0], test_values[0]), sep= ", ")

    print("\nTesting power amplifier...")
    amplifier = power_amplifier(fireball, 4)
    print(f"Value before: {test_values[1]}\n"
          f"Value after: {amplifier(test_targets[1], test_values[1])}")

    print("\nTesting conditional caster...")
    conditional = conditional_caster(condition, heal)
    print(conditional(test_targets[2], 20))
    print(conditional(test_targets[2], -20))

    spells = [fireball, heal]
    print("\nTesting sequence caster...")
    sequence = spell_sequence(spells)
    print("\n".join(sequence(test_targets[3], test_values[2])))


if __name__ == "__main__":
    main()