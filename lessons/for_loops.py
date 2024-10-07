"""Practice for using for loops."""

pets: list[str] = ["Louie", "Bo", "Bear"]

for pet in pets:
    print(f"Good boy, {pet}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for index in range(0, len(names)):
    print(f"{index}: {names[index]}")
