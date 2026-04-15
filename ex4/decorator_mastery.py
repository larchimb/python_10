from typing import Callable, Any
from time import time, sleep
from functools import wraps
import random


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable:
        print(f"Casting {func.__name__}...")
        init_time = time()
        ret = func(*args, **kwargs)
        timer = time() - init_time
        print(f"Spell completed in {timer:.3f} seconds")
        return ret
    return wrapper


def power_validator(min_power: int) -> Callable:
    def spell(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if len(args) <= 2:
                return "The function hasn't enought arguments"
            power = args[2]
            if not isinstance(power, int):
                return "The function hasn't the right arguments"
            elif power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(*args, **kwargs)
        return wrapper
    return spell


def retry_spell(max_attempts: int) -> Callable:
    def cast_spell(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Callable | str:
            attemps = 1
            while attemps <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attemps < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {attemps}/{max_attempts})")
                attemps += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return cast_spell


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for letter in name:
            if not (letter.isalpha() or letter.isspace()):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball(target: str, power: int) -> str:
    sleep(0.654)
    return f"Fireball hit {target} make him loose {power} HP"


@retry_spell(3)
def random_test() -> str:
    test = random.randint(0, 10)
    if test < 8:
        raise Exception(f"{test} is less than 8")
    return ("Success")


def main() -> None:

    try:
        print("Testing spell timer...")
        print(fireball("Dragon", 14))

        print("\nTesting retry_spell...")
        print(random_test())

        print("\nTesting MageGuild...")
        mage = MageGuild()
        print(mage.validate_mage_name("Alex Storm"))
        print(mage.validate_mage_name("L"))
        print(mage.cast_spell('fireball', 12))
        print(mage.cast_spell('fireball', 3))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
