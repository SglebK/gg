import  random

class Activity:
    def __init__(self, name: str, progress=100, feeling=100):
        self.name = name
        self.progress = progress
        self.feeling = feeling
        self.alive = True

class Student(Activity):
    def __str__(self):
        return F"{self.name} (успеваемость: {self.progress}, настроение: {self.feeling})"

    def do(self, activity: Activity):
        print(f"{self.name} взялся за {activity.name}")
        self.progress += activity.progress
        self.feeling += activity.feeling
        self.check_alive()

    def check_alive(self):
        self.alive = self.progress > 0 and self.feeling > 0

stud1 = Student(name = "Марк")
stud2 = Student(name = "Денис")

math = Activity("Математика", progress=4, feeling=-3)
english = Activity("Английський", progress=4, feeling=-6)
tv = Activity("Просмотр телевизора", progress=-2, feeling=3)
history = Activity("История", progress=4, feeling=-4)
football = Activity("Футбол", progress=-1, feeling=2)
computer_gaming = Activity("Компьютерни инры", progress=-2, feeling=5)

activities = [math, english, history, football, computer_gaming, tv]
for day in range(30):
    print(f" - День {day+1}")
    stud1.do(random.choice(activities))
    stud2.do(random.choice(activities))
    print(" --- ")
    print(stud1)
    print(stud2)
    if not stud1.alive or not stud2.alive:
        break