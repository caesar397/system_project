from typing import Protocol

class Firmy(Protocol):
    def __init__(self, id, nazwa, lat, lon):
        self.id = id
        self.nazwa = nazwa
        self.lat = lat
        self.lon = lon

class Pracownicy(Protocol):
    def __init__(self, id, imie, nazwisko, lat, lon, id_firmy):
        self.id = id
        self.imie = imie
        self.nazwisk = nazwisko
        self.lat = lat
        self.lon = lon
        self.id_firmy = id_firmy

