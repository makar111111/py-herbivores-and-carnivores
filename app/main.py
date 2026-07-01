class Animal:
    alive = []  # атрибут КЛАСУ — спільний для всіх

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)  # додаємо себе до списку живих

    def __repr__(self) -> str:
        # магічний метод — як виглядає об'єкт при print()
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden  # True → False → True → ...


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        # кусаємо тільки Herbivore і тільки якщо не ховається
        if not isinstance(other, Herbivore):
            return
        if other.hidden:
            return

        other.health -= 50

        # якщо здоров'я впало до 0 або нижче — тварина вмирає
        if other.health <= 0:
            other.health = 0
            Animal.alive.remove(other)
