# KOD STARTOWY

# class LabDevice:
#     def __init__(self, name: str):
#         self.name = name
#
#     def run_code(self, program: str):
#         return f"{self.name} uruchamia {program}"
#     def print_3d(self, model: str):
#         return f"{self.name} drukuje {model}"
#     def display(self, slide: str):
#         return f"{self.name} wyświetla {slide}"
#
# class Printer3D(LabDevice):
#     def run_code(self, program: str):
#         raise Exception("Drukarka nie uruchamia kodu!")
#     def display(self, slide: str):
#         raise Exception("Drukarka nie ma ekranu!")
#
# class SmartBoard(LabDevice):
#     def print_3d(self, model: str):
#         raise Exception("Tablica nie drukuje!")
#
#     def hackathon(devices: list[str]):
#         return [d.run_code("main.py") for d in devices]

# LSP
# Linie 11-15: Printer3D dziedziczy po LabDevice, ale metody run_code i display
# rzucają wyjątek zamiast działać. Obiekt klasy pochodnej nie może
# zastąpić obiektu klasy bazowej bez psucia programu
# hackathon wywołuje run_code więc jedna drukarka na liście psuje
# cały system. To samo dotyczy SmartBoard - metoda print_3d.

# ISP
# Linie 1-9: jedna klasa bazowa wymusza na każdym urządzeniu trzy metody
# (run_code, print_3d, display), choć żadne urządzenie nie potrzebuje
# wszystkich naraz. Klasy Printer3D i SmartBoard muszą więc dziedziczyć metody,
# których nie umieją, i zastępują je wyjątkami
# Dodatkowo linia 21: typ list[str] jest błędny, bo hackathon przyjmuje urządzenia,
# a nie napisy.

from abc import ABC, abstractmethod


class LabDevice:
    def __init__(self, name: str):
        self.name = name


class CodeRunner(ABC):
    @abstractmethod
    def run_code(self, program: str) -> str:
        pass


class Printer(ABC):
    @abstractmethod
    def print_3d(self, model: str) -> str:
        pass


class Display(ABC):
    @abstractmethod
    def display(self, slide: str) -> str:
        pass


class Workstation(LabDevice, CodeRunner, Display):
    def run_code(self, program: str) -> str:
        return f"{self.name} uruchamia {program}"

    def display(self, slide: str) -> str:
        return f"{self.name} wyświetla {slide}"


class Printer3D(LabDevice, Printer):
    def print_3d(self, model: str) -> str:
        return f"{self.name} drukuje {model}"


class SmartBoard(LabDevice, Display):
    def display(self, slide: str) -> str:
        return f"{self.name} wyświetla {slide}"


def hackathon(devices: list[CodeRunner]) -> list[str]:
    return [d.run_code("main.py") for d in devices]


def wyniki_pracownie() -> list[str]:
    pracownia_204: list[LabDevice] = [
        Workstation("Komputer 1"),
        Printer3D("Drukarka 3D"),
        SmartBoard("Tablica interaktywna"),
    ]
    wyniki = []
    for urzadzenie in pracownia_204:
        if isinstance(urzadzenie, CodeRunner):
            wyniki.append(urzadzenie.run_code("main.py"))
        if isinstance(urzadzenie, Printer):
            wyniki.append(urzadzenie.print_3d("model.stl"))
        if isinstance(urzadzenie, Display):
            wyniki.append(urzadzenie.display("slajd 1"))
    return wyniki


if __name__ == "__main__":
    for wynik in wyniki_pracownie():
        print(wynik)
    print(hackathon([Workstation("Komputer 2")]))