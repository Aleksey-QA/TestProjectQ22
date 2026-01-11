#Задание: Система пиццерии
#Создайте классы для моделирования пиццерии. Базовый класс Pizza содержит свойства:
# размер (small/medium/large), список ингредиентов (список строк), цена (float).
# Добавьте метод calculate_price(), который считает стоимость на основе размера и
# ингредиентов (например, базовая цена + 1$ за каждый ингредиент).
#• Наследование: Классы MeatPizza (с мясными ингредиентами, переопределите
# calculate_price() с наценкой 20%) и VeggiePizza (овощная, скидка 10%).
#• Инкапсуляция: Свойство _ingredients доступно только для чтения через геттер,
# метод add_ingredient() добавляет ингредиент с проверкой (не больше 10).
#• Полиморфизм: Абстрактный базовый класс Order с методом prepare(),
# переопределенный для PizzaOrder (печатает рецепт и цену).
#• Дополнительно: Класс Pizzeria с методом take_order(), который создает пиццу по
# выбору и выводит чек.
#Пример использования:
#pizza = MeatPizza("large", ["сыр", "пепперони"])
#order = PizzaOrder(pizza)
#order.prepare()  # Вывод: "Готовим мясную пиццу large: цена 25$"

from abc import ABC, abstractmethod
class Pizza:
    base_prices = {"small": 10, "medium": 15, "large": 20}

    def __init__(self, size: str, ingredients: list[str]):
        if size not in self.base_prices:
            raise ValueError("Размер должен быть один из: small, medium, large")
        self._size = size
        self._ingredients = list(ingredients)
        self.price = 0.0
        self.calculate_price()

    def get_ingredient(self):
        return list(self._ingredients)

    def add_ingredient(self, ingredients):
        if len(ingredients) <= 10:
            self._ingredients = ingredients
        else:
            print('Ингридиентов не может быть больше 10')
            self._ingredients = ['Cыр']
        self._ingredients.append(ingredients)
        self.calculate_price()

    def calculate_price(self):
        return self.base_prices[self._size] + len(self._ingredients)

    def __str__(self):
        return 'пиццу'

class MeatPizza(Pizza):
    def calculate_price(self):
        return round((self.base_prices[self._size] + len(self._ingredients)) * 1.2, 2)
    def __str__(self):
        return 'мясную пиццу'

class VeggiePizza(Pizza):
    def calculate_price(self):
        return round((self.base_prices[self._size] + len(self._ingredients)) * 0.9, 2)
    def __str__(self):
        return 'вегетарианскую пиццу'

class Order(ABC):
    def prepare(self):
        pass

class PizzaOrder(Order):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza
    def prepare(self):
        print(f'Готовим {self._pizza.__str__()} {self._pizza._size}: цена {self._pizza.calculate_price()}')
        print(f'Ингридиенты: {self._pizza.get_ingredient()}')

class Pizzeria:
    def take_order(self, pizza_type: str, size: str, ingridients: list[str]):
        pizza_type = pizza_type.lower()
        if pizza_type == "meat":
            pizza = MeatPizza(size, ingridients)
        elif pizza_type == "veggie":
            pizza = VeggiePizza(size, ingridients)
        else:
            raise ValueError("Неизвестный тип пиццы: выберите 'meat' или 'veggie'")
        pizza.calculate_price()
        return PizzaOrder(pizza)

pizza = MeatPizza("large", ["сыр", "пепперони", "помидоры", "чеснок"])
order = PizzaOrder(pizza)
order.prepare()
pizzaVegan = VeggiePizza("small", ["сыр", "пепперони", "помидоры", "шпинат"])
order = PizzaOrder(pizzaVegan)
order.prepare()
print()

pizzeria = Pizzeria()
order2 = pizzeria.take_order("meat", "large", ["бекон", "читос"])
order2.prepare()