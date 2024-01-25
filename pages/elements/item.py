from constants.locators import ItemLocators


class Item(object):
    title_locator = ItemLocators.ITEM_TITLE
    desc_locator = ItemLocators.ITEM_DESC
    price_locator = ItemLocators.ITEM_PRICE

    def __str__(self):
        return (
            f"title: {self.title}, description: {self.description}, price: {self.price}"
        )

    def __init__(self, container):

        self.title = container.find_element(*self.title_locator).text
        self.description = container.find_element(*self.desc_locator).text
        price = container.find_element(*self.price_locator).text
        self.price = float(price.replace("$", ""))

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return (
                self.title == other.title
                and self.description == other.description
                and self.price == other.price
        )

    def __repr__(self):
        return self.__str__()

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)


class QuantityItem(Item):
    quantity_locator = None

    def __init__(self, container):
        super().__init__(container)
        quantity = container.find_element(*self.quantity_locator)
        self.quantity = int(quantity.text)

    def __str__(self):
        return f"{super().__str__()}, quantity: {self.quantity}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, QuantityItem) and self.quantity == other.quantity:
            return True
        return super().__eq__(other)

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)
