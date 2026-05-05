from typing import Protocol

class Firmy(Protocol):
    def __init__(self, id, nazwa, lat, lon):
        self.id = id
        self.nazwa = nazwa
        self.lat = lat
        self.lon = lon

class Pracownicy(Protocol):
    def __init__(self, id, imie, nazwisko, firma):
        self.id = id
        self.imie = imie
        self.nazwisk = nazwisko
        self.firma = firma

class Wydarzenia(Protocol):
    def __init__(self, id, nazwa, lat, lon, firma):
        self.id = id
        self.nazwa = nazwa
        self.lat = lat
        self.lon = lon
        self.firma = firma


