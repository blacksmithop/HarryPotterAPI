from urllib.request import urlopen, Request
from json import loads
from random import choice

BASE_URL = 'https://www.potterapi.com/v1'
KEY = None


class Character(object):

    def __init__(self, dictionary):
        ...
        for k, v in dictionary.items():
            setattr(self, k, v)

    def __contains__(self, param1):
        return param1 in self.__dict__.keys()


class Spells(object):

    def __init__(self, dictionary):
        ...
        for k, v in dictionary.items():
            setattr(self, k, v)

    def __contains__(self, param1):
        return param1 in self.__dict__.keys()


class House(object):

    def __init__(self, dictionary):
        ...
        for k, v in dictionary.items():
            setattr(self, k, v)

    def __contains__(self, param1):
        return param1 in self.__dict__.keys()


def get_house(name: str):
    """
    :param name: Name of the Hogwarts house
    :return: Various facts
    """
    name = name.title()
    json = getdata(f"{BASE_URL}/houses/?key={KEY}")
    json = next((d for d in json if name == d['name']), None) or next((d for d in json if name in d['name']), None)
    if json is None:
        raise ValueError('Cannot find House on PotterAPI')
    del json['members']
    return House(json)


def random_house():
    """
    :return: Random Hogwarts house
    """
    data = getdata(f"{BASE_URL}/sortingHat/")
    return data


def get_character(name: str):
    """
    :param name: Name of the Character
    :return: Various facts
    """
    name = name.title()
    json = getdata(f"{BASE_URL}/characters/?key={KEY}")
    json = next((d for d in json if name == d['name']), None) or next((d for d in json if name in d['name']), None)
    if json is None:
        raise ValueError('Cannot find Character on PotterAPI')
    return Character(json)


def random_character():
    """
    :return: Random Character from HP
    """
    json = getdata(f"{BASE_URL}/characters/?key={KEY}")
    json = choice(json)
    return Character(json)


def get_spell(name: str):
    """
    :param name: Name of the Spell
    :return: Various facts
    """
    name = name.title()
    json = getdata(f"{BASE_URL}/spells/?key={KEY}")
    json = next((d for d in json if name == d['spell']), None) or next((d for d in json if name in d['spell']), None)
    if json is None:
        raise ValueError('Cannot find Spell on PotterAPI')
    return Spells(json)


def random_spell():
    """
    :return: Random Spell from HP
    """
    json = getdata(f"{BASE_URL}/spells/?key={KEY}")
    json = choice(json)
    return Spells(json)


def getdata(url):
    req = Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/35.0.1916.47 Safari/537.36 '
        }
    )
    f = urlopen(req)
    data = loads(f.read().decode('utf-8'))
    f.close()
    return data
