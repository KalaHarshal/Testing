class Parrot:
    # Class-level attribute to keep track of the unique number
    _unique_number_counter = 7001

    def __init__(self, name, color):
        # Private attributes
        self.__name = name
        self.__color = color
        self.__unique_number = Parrot._unique_number_counter

        # Increment the counter for the next parrot
        Parrot._unique_number_counter += 1

    # Getter method for name
    def get_name(self):
        return self.__name

    # Getter method for color
    def get_color(self):
        return self.__color

    # Getter method for unique number
    def get_unique_number(self):
        return self.__unique_number

    # Method to display parrot details
    def display_parrot_details(self):
        print("Parrot Name:", self.get_name())
        print("Color:", self.get_color())
        print("Unique Number:", self.get_unique_number())
        print()


# Creating instances of Parrot class
parrot1 = Parrot("Rio", "Green")
parrot2 = Parrot("Sky", "Blue")
parrot3 = Parrot("Coco", "Yellow")
parrot4 = Parrot("Bella", "Red")

# Displaying the details of each parrot
parrot1.display_parrot_details()
parrot2.display_parrot_details()
parrot3.display_parrot_details()
parrot4.display_parrot_details()
