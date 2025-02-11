class UnitConverter:
    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers * 0.621371

    @staticmethod
    def miles_to_kilometers(miles):
        return miles / 0.621371

if __name__ == "__main__":

    print(f"5 kilometers is {UnitConverter.kilometers_to_miles(5)} miles")
    print(f"3 miles is {UnitConverter.miles_to_kilometers(3)} kilometers")

