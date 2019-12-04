class Person():
    """一个人类，作为父类"""
    def __init__(self,name,age,sex):
        """父类初始化方法"""
        self.name = name;
        self.age = 23
        self.sex = sex;
 
    def get_desc_info(self):
        print("姓名为：" + self.name + "，年龄为：" + str(self.age) + "，性别为：" + self.sex);
		
class Student(Person):
    """一个学生类，作为子类"""
    def __init__(self,name,age,sex):
        """子类初始化方法"""
        super().__init__(name,age,sex)
        self.major = '软件工程'
        self.number = '2012131739'
        self.year = 4
    
    def get_student_info(self):
        print("该学生的姓名为：" + self.name + "，年龄为：" + str(self.age) + "，性别为：" + self.sex + ",专业为：" + self.major + ",学号为："+ str(self.year) );
		
student = Student('林梓然',26,'男');
student.get_student_info()
