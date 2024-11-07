def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5 / 9

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    tempInCelsius = float(input("Temperature in Celsius: "))
    convert = CelsiusToKelvin(tempInCelsius)
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")
    print(str(convert.conversion()) + " Kelvin")

    tempInFahrenheit = float(input("Temperature in Fahrenheit: "))
    convert = FahrenheitToCelsius(tempInFahrenheit)
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Celsius")
    print(str(convert.conversion()) + " Kelvin")

    tempInKelvin = float(input("Temperature in Kelvin: "))
    convert = KelvinToCelsius(tempInKelvin)
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")
    print(str(convert.conversion()) + " Celsius")

main()