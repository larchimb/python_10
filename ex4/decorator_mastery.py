from typing import Callable
from time import time
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
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
        def wrapper(*args, **kwargs):
            if len(args) <= 2:
                return "The function hasn't enought arguments"
            power = args[2]
            print(power)
            if not power:
                return "The function hasn't the right arguments"
            elif power < min_power:
                return "Insufficient power for this spell"
            else:
                return func(*args, **kwargs)
        return wrapper
    return spell



def retry_spell(max_attempts: int) -> Callable:
    pass

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


def main() -> None:
    mage = MageGuild()

    mage.validate_mage_name("Lolopiop")
    print(mage.cast_spell('fireball', 12))


if __name__ == "__main__":
    main()