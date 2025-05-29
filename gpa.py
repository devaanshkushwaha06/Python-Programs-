class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        if self.hours == 0:
            return 0.0  # Avoid division by zero
        return self.qpoints / self.hours

def find_best_gpa(filename="student_data.txt"):
    best_student = None
    highest_gpa = -1.0

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split()
                    if len(parts) >= 3:
                        name_parts = parts[:-2]
                        name = " ".join(name_parts).rstrip(',')
                        try:
                            hours = float(parts[-2])
                            qpoints = float(parts[-1])
                            student = Student(name, hours, qpoints)
                            student_gpa = student.gpa()
                            if student_gpa > highest_gpa:
                                highest_gpa = student_gpa
                                best_student = student
                        except ValueError:
                            print(f"Skipping invalid data line: {line}")
                    else:
                        print(f"Skipping incomplete data line: {line}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return best_student

if __name__ == "__main__":
    with open("student_data.txt", "w") as f:
        f.write("sanskriti 127 228\n")
        f.write("Mrigank 37.5 137\n")
        f.write("kanishka 18 41.5\n")
        f.write("Devaansh 100 400\n")
        f.write("Bhuvendra 200 150\n")

    best_student = find_best_gpa()

    if best_student:
        print("Student with the best GPA:")
        print(f"Name: {best_student.getName()}")
        print(f"Credit Hours: {best_student.getHours()}")
        print(f"GPA: {best_student.gpa():.2f}")
    else:
        print("No student data found or an error occurred.")