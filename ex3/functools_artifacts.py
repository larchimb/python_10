from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if not operation in operations.keys():
        raise Exception(f"{operation} is not support")

    return reduce(operations[operation], spells)

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_spell = partial(attack, 50, "fire")
    air_spell = partial(attack, 50, "air")
    thunder_spell = partial(attack, 50, "thunder")
    return {"fire": fire_spell, "air": air_spell, "thunder": thunder_spell}

@lru_cache(maxsize= None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

@singledispatch
def spell_dispatcher() -> Callable[[Any], str]:
    pass

def attack(power: int, element: str, target: str) -> str:
    return f"{element.capitalize()} attack makes {target} loose {power} HP"

def test_reducer() -> None:
    spell_powers = [1, 2, 4, 5]
    operations = ['add', 'multiply', 'max', 'min']
    try:
        for operation in operations:
            print(f"{operation.capitalize()}: "
                  f"{spell_reducer(spell_powers, operation)}")

        print(f"Error: {spell_reducer(spell_powers, 'test')}")
    except Exception as e:
        print(e)

def test_partial() -> None:
    try:
        p_e = partial_enchanter(attack)
        print(p_e['fire']("Wizard"))
        print(p_e['air']("Dragon"))
        print(p_e['thunder']("Goblin"))
        print(p_e['water']("Goblin"))
    except (KeyError, Exception) as e:
        print(f"{e} is not in the dictionnary")

def test_fib() -> None:
    try:
        tests = [0, 1, 55, 40, 1900]
        for nb in tests:
            print(f"Fib({nb}): {memoized_fibonacci(nb)}")
            print(memoized_fibonacci.cache_info())
    except (RecursionError, Exception) as e:
        print(e)

    try:
        print("\nTesting memoized fibonacci...")
        tests = [0, 1, 55, 40, 1000, 1900]
        for nb in tests:
            print(f"Fib({nb}): {memoized_fibonacci(nb)}")
            print(memoized_fibonacci.cache_info())
    except (RecursionError, Exception) as e:
        print(e)



def main () -> None:

    print("Testing spell reducer...")
    test_reducer()

    print("\nTesting partial enchantment...")
    test_partial()

    print("\nTesting memoized fibonacci...")
    test_fib()

if __name__ == "__main__":
    main()