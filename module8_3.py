class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = None
        self.__numbers = None
        try:
            self.__vin = self.__validate_vin(vin)
        except IncorrectVinNumber as exc:
            print(exc.message)
        try:
            self.__numbers = self.__validate_numbers(numbers)
        except IncorrectCarNumbers as exc:
            print(exc.message)

    @staticmethod
    def __validate_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return vin_number

    @staticmethod
    def __validate_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return numbers


first = Car('Model1', 1000000, 'f123dj')
print(f'{first.model}, vin: {first.__vin}, numbers: {first.__numbers}')

second = Car('Model2', 300, 'т001тр')
print(f'{second.model}, vin: {second.__vin}, numbers: {second.__numbers}')

third = Car('Model3', 2020202, 'нет номера')
print(f'{third.model}, vin: {third.__vin}, numbers: {third.__numbers}')
