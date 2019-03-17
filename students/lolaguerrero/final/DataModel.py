# Desc: Python 210 Final - Data Object Model Classes
# ChangeLog: (When,Who,What)
# 03/14/19, Lola Guerrero, Created Script

from datetime import datetime

class Product(object):

    def __init__(self, product_id: int, product_name: str):
        self.__product_id = product_id
        self.__product_name = product_name

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id):
        if type(product_id) is not int:
            raise TypeError("Requires integer!")
        if product_id <= 0:
            raise ValueError("Requires value greater than zero!")
        else: self.__product_id = product_id

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):
        self.__product_name = str(product_name).strip()

    def __str__(self):
        return '{0},{1}'.format(self.product_id, self.product_name)

    def __repr__(self):
        return "{0}:[{1}]".format("Product",str(self.__dict__()))

    def __dict__(self):
        return {"product_id": self.product_id, "product_name": self.product_name}

    #Comparisons
    __comparison_err_message = "One or both are not Product objects!"

    def __eq__(self, other):
        if not isinstance(other, Product):
            raise TypeError(self.__comparison_err_message)
        return self.product_id == other.product_id and self.product_name == other.product_name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Product):
            raise TypeError(self.__comparison_err_message)
        return self.product_id > other.product_id

    def __lt__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        if not isinstance(other, Product):
            raise TypeError(self.__comparison_err_message)
        return self.product_id >= other.product_id

    def __le__(self, other):
        return not self.__ge__(other)



class Inventory(object):
    def __init__(self, inventory_id: int, inventory_date: datetime.date):
        self.__inventory_id = inventory_id
        self.__inventory_date = inventory_date

    @property
    def inventory_id(self):
        return self.__inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):
        __inventory_id = inventory_id

    @property
    def inventory_date(self):
        return self.__inventory_date

    @inventory_date.setter
    def inventory_date(self, inventory_date):
        __inventory_date = inventory_date

    def __str__(self):
        return '{0},{1}'.format(self.inventory_id, self.inventory_date)

    def __repr__(self):
        return "{0}:[{1}]".format("Inventory", str(self.__dict__()))

    def __dict__(self):
        return {"inventory_id": self.inventory_id, "inventory_date": self.inventory_date}



class InventoryCount(object):

    def __init__(self, inventory: Inventory, product: Product, product_inventory_count: int):
        self.__inventory = inventory
        self.__product = product
        self.__count = product_inventory_count

    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self, inventory: Inventory):
        self.__inventory = inventory

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, product: Product):
        self.__product = product

    @property
    def product_inventory_count(self):
        return self.__count

    @product_inventory_count.setter
    def product_inventory_count(self, count: int):
        __count = count

    def __str__(self):
        return '{0},{1},{2}'.format(self.inventory, self.product, self.product_inventory_count)

    def __repr__(self):
        return "{i}:[{p}, {c}:{cv}]".format(i="InventoryCount",
                                            p=self.product.__repr__(),
                                            c="product_inventory_count",
                                            cv=self.product_inventory_count)

    def __dict__(self):
        return {"inventory_id": self.inventory.inventory_id,
                "product_id": self.product.product_id,
                "product_inventory_count": self.product_inventory_count}