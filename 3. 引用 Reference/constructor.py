class Student:
    def __init__(self, name, score): # 构造函数
        self.name = name
        self.score = score
        self.speak()

    def speak(self):
        print('Name: ', self.name, 'Score: ', self.score)

if __name__=='__main__':
    stu_1= Student('Jack', 80)
    #stu_1.speak()

    stu_2 = Student('John', 89)
    #stu_2.speak()

