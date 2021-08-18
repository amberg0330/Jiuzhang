# coding=utf-8
class Student:
    def __init__(self, name, score=100):
        self.name = name
        self.score = score

    def speak(self):
        print(self.name, self.score)


def run_student_example1():
    print('Student example 1')
    student_1 = Student('Tom')
    student_2 = Student('Jack')
    student_1.speak()
    student_2.speak()

    student_2.name = 'Jerry'
    student_1.speak()
    student_2.speak()


def run_student_example2():
    print('Student example 2')
    student_1 = Student('Tom')
    student_2 = student_1 #并非原样复制！！
    student_1.speak()
    student_2.speak()

    student_2.name = 'Jerry'
    student_1.speak()
    student_2.speak()


def run_student_example3():
    print('Student example 3')
    student_1 = Student('Tom')
    student_2 = Student('Jack')
    student_1.speak()
    student_2.speak()

    t = student_1
    student_1 = student_2
    student_2 = t

    student_1.speak()
    student_2.speak()


if __name__ == '__main__':
    list_1 = [12, 15.6, True, 'hello', ['a', 'b']]
    list_2 = list_1
    print(id(list_1), id(list_2), list_1 is list_2)

    list_1[1] = -3
    print(id(list_1), id(list_2), list_1 is list_2)

    list_2 = list_1[:]
    print(id(list_1), id(list_2), list_1 is list_2, list_1 == list_2)

    my_tuple = (1, 2, 'abc', [6, 7], 12.3, True)
    my_tuple[3].append(20)
    print(my_tuple)
