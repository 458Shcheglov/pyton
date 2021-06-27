class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surnae = surname
        self.position = position
        self._income = {'profit': wage, "bonus": bonus, 'some': 800}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surnae}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"

manager = Position("Tom", "Cruse", "CEO", 50000, 125000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_full_profit())

