class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def speak(self):
        print(self.name, self.score)

if __name__ == '__main__':
    student = Student('Jack', 80)
    print(student.name, student.score)
    student.speak()

    student.score=98
    print(student.name, student.score)
    student.speak()

