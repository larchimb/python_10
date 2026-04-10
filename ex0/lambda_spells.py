from typing import Union


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: (f"* {s} *"), spells))


def mage_stats(mages: list[dict]) -> dict[str,Union[int, float]]:
    dic: dict[str,Union[int, float]] = {}
    dic["max"] = max(mages, key=lambda m: m["power"])["power"]
    dic["min"] = min(mages, key=lambda m: m["power"])["power"]
    dic["avg_power"] = round(
        sum(map(lambda m: m["power"], mages)) / len(mages), 2
        )

    return dic


def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 80, "type": "relic"},
        {"name": "Lightning Rod", "power": 111, "type": "accessory"},
        {"name": "Wind Cloak", "power": 89, "type": "focus"},
        {"name": "Ice Wand", "power": 114, "type": "weapon"},
    ]
    mages = [
        {"name": "Riley", "power": 59, "element": "water"},
        {"name": "Luna", "power": 70, "element": "lightning"},
        {"name": "River", "power": 83, "element": "light"},
        {"name": "Rowan", "power": 55, "element": "wind"},
    ]
    spells = ["earthquake", "flash", "blizzard", "shield"]

    artifacts_sorted = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    for a in artifacts_sorted:
        print(f"{a['name']} ({a['power']})")

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("Mages stats")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
