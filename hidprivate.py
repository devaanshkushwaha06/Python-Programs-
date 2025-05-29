class Student(object):
    def __init__(self, first, last, age):
        self.first = first
        self._last = last
        self.__age = age

    def get_attribute(self, visibility):
        result = {}
        if visibility == "public":
            result['first'] = self.first
        elif visibility == "private":
            result['age'] = self.__age
        elif visibility == "protected":
            result['last'] = self._last
        elif visibility == "all":
            result['first'] = self.first
            result['last'] = self._last
            result['age'] = self.__age
        else:
            raise ValueError("Invalid type. Choose from 'public', 'private', 'protected', or 'all'.")
        return result

def main():
    aStudent = Student("Devaansh", "Kushwaha", 19)
    print("Public:", aStudent.get_attribute("public"))
    print("Protected:", aStudent.get_attribute("protected"))
    print("Private:", aStudent.get_attribute("private"))
    print("All:", aStudent.get_attribute("all"))

if __name__ == "__main__":
    main()