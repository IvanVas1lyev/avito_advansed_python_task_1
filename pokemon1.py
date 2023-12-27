from abc import ABC, abstractmethod


class PokemonTrainInterface(ABC):
    @abstractmethod
    def increase_experience(self, value):
        """Увеличивает опыт покемона на заданное значение."""
        pass

    @property
    @abstractmethod
    def experience(self):
        """Возвращает текущий опыт покемона."""
        pass


class BasePokemon(PokemonTrainInterface):
    def __init__(self, name: str, poketype: str):
        """
        Инициализирует экземпляр класса BasePokemon.

        Args:
            name (str): Имя покемона.
            poketype (str): Тип покемона.
        """
        self.name = name
        self.poketype = poketype
        self._experience = 100

    def increase_experience(self, value):
        """
        Увеличивает опыт покемона на заданное значение.

        Args:
            value: Значение, на которое увеличивается опыт.
        """
        self._experience += value

    @property
    def experience(self) -> int:
        """
        Возвращает текущий опыт покемона.

        Returns:
            int: Текущий опыт покемона.
        """
        return self._experience


if __name__ == '__main__':
    bulbasaur = BasePokemon(name='Bulbasaur', poketype='grass')
    bulbasaur.increase_experience(100)
    bulbasaur.increase_experience(100)

    assert bulbasaur.experience == 300, 'Try harder, Neeman'
