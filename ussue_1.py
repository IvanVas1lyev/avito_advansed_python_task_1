"""
First task advanced python avito
"""
from keyword import kwlist
from typing import Dict
import json


class JsonParser:
    """
    Сlass that expands a dictionary into an object whose fields
    can be accessed through a dot.

    Works through recursive calls.
    """
    def __init__(self, json_data: Dict) -> None:
        """
        JsonParser initiliazation.

        Parameters
        ----------
        json_data : Dict
            A dictionary that is directly obtained from json data.
        """
        for key, value in json_data.items():
            if key in kwlist:
                key = key + "_"
            if isinstance(value, dict):
                setattr(self, key, JsonParser(value))
            else:
                setattr(self, key, value)


class ColorizeMixin:
    """
    Class-mixin designed for coloring output.
    """
    repr_color = 33

    def colored_repr(self, data: str) -> str:
        """
        Method that colors the passed string a fixed color.

        Parameters
        ----------
        data : str
            Text data for coloring.

        Returns
        -------
        str
            Colored text data.
        """
        return f'\033[1;{self.repr_color}m{data}'


class Advert(ColorizeMixin, JsonParser):
    """
    Class that expands a dictionary into an object with access
    to fields through a dot.

    Checks the price field for non-negativity, checks for the
    presence of the title field.
    """
    def __init__(self, mapping: Dict) -> None:
        """
        Advert initiliazation.

        Parameters
        ----------
        mapping : Dict
            A dictionary that is directly obtained from json data.
        """
        if 'title' not in mapping:
            raise ValueError('Mapping must contain field "title"')

        super().__init__(mapping)

    def __repr__(self):
        """
        Repr method for Advert class. Сalls a function 'colored_repr'
        to color text.

        Returns
        -------
        str
            Colored text data.
        """
        return self.colored_repr(data=f"{self.title} | {self.price} ₽")

    @property
    def price(self):
        """
        Special property 'price' of Advert class.
        If 'price' is not defined, retunrs 0.
        """
        return getattr(self, "price_", 0)

    @price.setter
    def price(self, value):
        """
        Price property setter.  
        If value is smaller than zero, raise ValueError.

        Parameters
        ----------
        value : int
            Value to set.
        """
        if value >= 0:
            setattr(self, "price_", value)
        else:
            raise ValueError('Price must be greater of equal than 0')


if __name__ == '__main__':
    json_obj = '''
    {
        "title": "Iphone 17 SUPERPRO PLUS",
        "price": 100000000,
        "location": {
            "address": "город Москва, Лениниские горы 1",
            "metro_stations": [
                "Раменки",
                "Университет",
                "Ломоносовский проспект"
            ]
        }
    }
    '''
    json_obj = json.loads(json_obj)
    data_obj = Advert(json_obj)

    print(data_obj.location.address)
    print(data_obj.price)
    print(data_obj)
    