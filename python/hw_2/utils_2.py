import json
import keyword


class ColorizeMixin:
    """
    ClassMixin for print colour change

    Args for init:
    - repr_color_code: code of the certain colour

    """
    def __init__(self, repr_color_code: int = 32):
        self.repr_color_code = repr_color_code

    def __repr__(self):
        return f"\033[1;{self.repr_color_code};10m{self.title} | {self.price} ₽"


class AdvertBase(object):
    """
    Class for dynamic initialization of advertisement
    processed dynamically with setattr:
    - to avoid entanglement with keywords
    - to achieve .attribute access

    Args for init:
    - json_dict: json file with advertisement
    preliminarily transformed to python dict format

    """

    def __init__(self, json_dict):
        for key, value in json_dict.items():
            # if key is a keyword - add underscore to its name
            super.__setattr__(self, key + '_' if keyword.iskeyword(key) else key, value)

            # if value is a dict, then make subattributes of attribute
            if type(value) == dict:
                # see on stackoverflow this lambda "dam", not sure why it works
                self.__dict__[key] = lambda: None
                # add subattributes dynamically
                for k, v in value.items():
                    super.__setattr__(getattr(self, key), k, v)

        self.check_price()

    def check_price(self):
        """
        Price correctness check

        If there is no price, set to 0; if price < 0 - raise error

        """
        if 'price' not in self.__dict__:
            self.price = 0

        if self.price < 0:
            raise ValueError('must be >= 0')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class Advert(ColorizeMixin, AdvertBase):
    def __init__(self, json_dict):
        # yellow colour corresponds to repr_color_code=33
        ColorizeMixin.__init__(self, repr_color_code=33)
        AdvertBase.__init__(self, json_dict)


if __name__ == '__main__':

    lesson_str = """{
        "title": "python", "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
    }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    print('Test 1 from task example (subattribute of attribute): ')
    print(lesson_ad.location.address)
    print()

    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)

    print('Test 2 from task example (incorrect price): ')
    try:
        lesson_ad = Advert(lesson)
        print('Test failed')
    except ValueError:
        print('ValueError error mistake was raised')
    print()

    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)

    print('Test 3 from task example (no price): ')
    print(lesson_ad.price)
    print()

    iphone_str = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""

    iphone = json.loads(iphone_str)
    iphone_ad = Advert(iphone)

    print('DoD point 1:')
    print('iphone_ad.price', iphone_ad.price)
    print()

    print('DoD points 2-4: implemented or checked before')
    print()

    print('DoD point 5:')
    print('iphone_ad.location.address', iphone_ad.location.address)
    print()

    corgi_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""

    corgi = json.loads(corgi_str)
    corgi_ad = Advert(corgi)

    print('DoD point 6:')
    print('corgi_ad.class_', corgi_ad.class_)
    print()

    print('DoD point 7:')
    print(corgi_ad)
