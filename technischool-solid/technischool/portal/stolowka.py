# KOD STARTOWY

#class CanteenOrder:
#     BASE_PRICE = 20
#
#     def __init__(self, dish: str, customer: str):
#         self.dish = dish
#         self.customer = customer

#     def price(self):
#         if self.customer == "uczen":
#             return self.BASE_PRICE * 0.5
#         elif self.customer == "nauczyciel":
#             return self.BASE_PRICE * 0.8
#         elif self.customer == "gosc":
#             return self.BASE_PRICE

#     def print_receipt(self):
#         return f"{self.dish} | {self.customer} | {self.price()} zł"

# SRP
# - Klasa CanteenOrder ma trzy powody do zmiany:
#   * przechowywanie zamówienia (linie 3-5),
#   * liczenie ceny wg rodzaju klienta (linie 6-12, metoda price),
#   * drukowanie paragonu (linie 13-14, metoda print_receipt).
#   Zmiana cennika albo wyglądu paragonu wymusza edycję tej samej klasy.

# OCP
# - Linie 7-12 (łańcuch if/elif w price): każdy nowy rodzaj klienta (np. praktykant)
#   wymaga edycji istniejącej metody, zamiast dopisania nowej klasy.
# - Linia 12 i brak gałęzi else: nieznany klient daje None zamiast ceny,
#   więc dopisanie nowego typu bez zmiany price() psuje paragon.
# - Linia 5: klient jest zwykłym tekstem, więc zachowanie zależy od porównywania napisów.


from abc import ABC, abstractmethod

BASE_PRICE = 20


class Customer(ABC):
    nazwa: str

    @abstractmethod
    def price(self, base: float) -> float:
        pass


class Student(Customer):
    nazwa = "uczen"

    def price(self, base: float) -> float:
        return base * 0.5


class Teacher(Customer):
    nazwa = "nauczyciel"

    def price(self, base: float) -> float:
        return base * 0.8


class Guest(Customer):
    nazwa = "gosc"

    def price(self, base: float) -> float:
        return base


class CanteenOrder:
    def __init__(self, dish: str, customer: Customer):
        self.dish = dish
        self.customer = customer


class ReceiptPrinter:
    def print_receipt(self, order: CanteenOrder) -> str:
        cena = order.customer.price(BASE_PRICE)
        return f"{order.dish} | {order.customer.nazwa} | {cena:.2f} zł"


# Nowy rodzaj klienta dopisany bez zmieniania żadnej istniejącej klasy.
class Intern(Customer):
    nazwa = "praktykant"

    def price(self, base: float) -> float:
        return 0


def wyniki_stolowka() -> list[str]:
    printer = ReceiptPrinter()
    klienci = [Student(), Teacher(), Guest(), Intern()]
    return [printer.print_receipt(CanteenOrder("Pierogi z serem", k)) for k in klienci]


if __name__ == "__main__":
    for paragon in wyniki_stolowka():
        print(paragon)
