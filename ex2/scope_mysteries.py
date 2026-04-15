from typing import Callable


def mage_counter() -> Callable:
    counter = 0

    def increment() -> int:
        nonlocal counter
        counter += 1
        return counter
    return increment


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulate(value: int) -> int:
        nonlocal power
        power += value
        return power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    type = enchantment_type

    def enchantment(item: str) -> str:
        return f"{type} {item}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    dic: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        dic[key] = value

    def recall(key: str) -> int | str:
        return dic.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:

    power_additions = [7, 14, 17, 17, 10]
    enchantment_types = ['Shocking', 'Flaming', 'Radiant']
    items_to_enchant = ['Shield', 'Sword', 'Ring', 'Amulet']

    print("\nTesting mage counter")
    mage_counter_a = mage_counter()
    mage_counter_b = mage_counter()
    for i in range(3):
        print(f"counter_a call: {mage_counter_a()}")
    print(f"counter_b call: {mage_counter_b()}")

    print("\nTesting spell accumulator")
    accumulator = spell_accumulator(100)
    for value in power_additions:
        print(f"Base 100: add {value}: {accumulator(value)}")

    print("\nTesting enchantment factory")
    schock = enchantment_factory(enchantment_types[0])
    flame = enchantment_factory(enchantment_types[1])
    for item in items_to_enchant:
        print(schock(item))
        print(flame(item))

    print("\nTesting memory vault")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault['store']('secret', 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'secret': {vault['recall']('random')}")


if __name__ == "__main__":
    main()
