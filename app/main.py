class Animal:
    alive: list["Animal"] = []  # ← виправлено: type annotation (checklist #9)

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health  # ← тепер приймає health ззовні, або 100 за замовч.
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def __init__(self, name: str, health: int = 100) -> None:
        super().__init__(name, health)  # ← передаємо обидва в батька

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def __init__(self, name: str, health: int = 100) -> None:
        super().__init__(name, health)  # ← те саме для Carnivore

    def bite(self, other: Animal) -> None:
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return

        other.health -= 50

        if other.health <= 0:
            other.health = 0
            Animal.alive.remove(other)
