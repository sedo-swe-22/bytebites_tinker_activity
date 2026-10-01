"""
the list of classes
- Customer : keep name and past purchase history, the system can verify they are real users.
- FoodItem : track the name, price, category, and popularity rating
- Menu : the full collection of items — filter by category, sort by popularity rating
- Transaction : store the selected items and compute the total cost

"""


class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        self.items.append(item)

    def filter_by_category(self, category: str) -> list[FoodItem]:
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self) -> list[FoodItem]:
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    def __init__(self):
        self.items: list[FoodItem] = []

    def add_item(self, item: FoodItem) -> None:
        self.items.append(item)

    def compute_total_cost(self) -> float:
        return sum(item.price for item in self.items)


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history: list[Transaction] = []

    def add_purchase(self, transaction: Transaction) -> None:
        self.purchase_history.append(transaction)


if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 8.99, "Entrees", 4.5)
    soda = FoodItem("Large Soda", 2.50, "Drinks", 3.0)
    fries = FoodItem("Fries", 3.50, "Sides", 4.8)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(fries)

    drinks = menu.filter_by_category("Drinks")
    assert drinks == [soda]

    by_popularity = menu.sort_by_popularity()
    assert by_popularity == [fries, burger, soda]

    transaction = Transaction()
    transaction.add_item(burger)
    transaction.add_item(soda)
    assert transaction.compute_total_cost() == burger.price + soda.price

    customer = Customer("Alex")
    customer.add_purchase(transaction)
    assert customer.purchase_history == [transaction]

    print("All checks passed.")
