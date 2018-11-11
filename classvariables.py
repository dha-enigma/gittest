class BestCourse:
     website = "http://github.com"

     def __init__(self, name):
         self.name = name

python_course = BestCourse("Learn Python")
learn_command_line = BestCourse("Learn Command Line")

print(python_course.name)
print(BestCourse.website)
print("\n")
print(learn_command_line.name)
print(BestCourse.website)
