from models import Customer, FoodItem, Menu, Transaction


def test_transaction_total_cost():
    # If a user adds a $10 burger and a $5 soda, does the total equal $15?
    burger = FoodItem("Burger", 10.0, "Entrees", 4.0)
    soda = FoodItem("Soda", 5.0, "Drinks", 3.0)

    transaction = Transaction()
    transaction.add_item(burger)
    transaction.add_item(soda)

    assert transaction.compute_total_cost() == 15.0


def test_menu_filter_by_category():
    # If the menu has a burger (Entrees) and a soda (Drinks), does filtering
    # by "Drinks" return only the soda?
    burger = FoodItem("Burger", 10.0, "Entrees", 4.0)
    soda = FoodItem("Soda", 5.0, "Drinks", 3.0)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)

    assert menu.filter_by_category("Drinks") == [soda]


def test_menu_filter_by_category_no_match():
    # If no item on the menu is in the queried category, does filtering
    # return an empty list instead of crashing?
    menu = Menu()
    menu.add_item(FoodItem("Burger", 10.0, "Entrees", 4.0))

    assert menu.filter_by_category("Drinks") == []


def test_menu_filter_by_category_multiple_matches():
    # If two items share a category, does filtering return both, in order?
    soda = FoodItem("Soda", 5.0, "Drinks", 3.0)
    lemonade = FoodItem("Lemonade", 4.0, "Drinks", 4.0)

    menu = Menu()
    menu.add_item(soda)
    menu.add_item(lemonade)

    assert menu.filter_by_category("Drinks") == [soda, lemonade]


def test_menu_sort_by_popularity():
    # If the menu has items rated 3, 5, and 4, does sorting by popularity
    # return them highest-to-lowest?
    soda = FoodItem("Soda", 5.0, "Drinks", 3.0)
    fries = FoodItem("Fries", 3.5, "Sides", 5.0)
    burger = FoodItem("Burger", 10.0, "Entrees", 4.0)

    menu = Menu()
    menu.add_item(soda)
    menu.add_item(fries)
    menu.add_item(burger)

    assert menu.sort_by_popularity() == [fries, burger, soda]


def test_menu_sort_by_popularity_empty():
    # If the menu has no items, does sorting return an empty list?
    menu = Menu()

    assert menu.sort_by_popularity() == []


def test_menu_sort_by_popularity_single_item():
    # If the menu has exactly one item, does sorting just return that item?
    burger = FoodItem("Burger", 10.0, "Entrees", 4.0)

    menu = Menu()
    menu.add_item(burger)

    assert menu.sort_by_popularity() == [burger]


def test_menu_sort_by_popularity_tie():
    # If two items have the same popularity rating, are both still present
    # and kept in their original (insertion) order?
    soda = FoodItem("Soda", 5.0, "Drinks", 4.0)
    fries = FoodItem("Fries", 3.5, "Sides", 4.0)

    menu = Menu()
    menu.add_item(soda)
    menu.add_item(fries)

    assert menu.sort_by_popularity() == [soda, fries]


def test_transaction_total_cost_empty():
    # If a user opens a transaction but adds nothing, does the system
    # return $0 or crash?
    transaction = Transaction()

    assert transaction.compute_total_cost() == 0


def test_food_item_stores_attributes():
    # Does a FoodItem store exactly what it was constructed with?
    burger = FoodItem("Burger", 10.0, "Entrees", 4.5)

    assert burger.name == "Burger"
    assert burger.price == 10.0
    assert burger.category == "Entrees"
    assert burger.popularity_rating == 4.5


def test_customer_purchase_history_empty_by_default():
    # Does a freshly created customer start with no purchase history?
    customer = Customer("Alex")

    assert customer.purchase_history == []


def test_customer_add_purchase():
    # If a customer completes a transaction, does it show up in their
    # purchase history?
    transaction = Transaction()
    transaction.add_item(FoodItem("Burger", 10.0, "Entrees", 4.0))

    customer = Customer("Alex")
    customer.add_purchase(transaction)

    assert customer.purchase_history == [transaction]


def test_customer_add_purchase_multiple():
    # If a customer completes two transactions, do both show up in their
    # purchase history, in the order they were added?
    first = Transaction()
    first.add_item(FoodItem("Burger", 10.0, "Entrees", 4.0))

    second = Transaction()
    second.add_item(FoodItem("Soda", 5.0, "Drinks", 3.0))

    customer = Customer("Alex")
    customer.add_purchase(first)
    customer.add_purchase(second)

    assert customer.purchase_history == [first, second]
