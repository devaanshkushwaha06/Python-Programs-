class Student(object):
    def __init__(self, first, last, age):
        self.__name = first
        self.__lastname = last
        self.__age = age

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, first):
        self.__name = first

    # Getter for lastname
    def get_lastname(self):
        return self.__lastname

    # Setter for lastname
    def set_lastname(self, last):
        self.__lastname = last

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Invalid age. Age must be a positive integer.")

def main():
    aStudent = Student("Devaansh", "Kushwaha", 19)
    print("Initial Name:", aStudent.get_name())
    print("Initial Lastname:", aStudent.get_lastname())
    print("Initial Age:", aStudent.get_age())

    # Using the setters
    aStudent.set_name("Vatsal")
    aStudent.set_lastname("Vaibhav")
    aStudent.set_age(23)

    print("\nUpdated Name:", aStudent.get_name())
    print("Updated Lastname:", aStudent.get_lastname())
    print("Updated Age:", aStudent.get_age())


if __name__ == "__main__":
    main()