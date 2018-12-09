from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    age = models.IntegerField(null=True, blank=True)
    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name

class Driver(Person):
    driver_id = models.AutoField(primary_key = True)
    def getName(self):
        return self.getFirstName()

class Student(Person):
    
    NORMAL = 'NORM'
    PROBLEM = 'PROB'
    STATUS_CHOICE = (
        (NORMAL, 'ปกติ'), 
        (PROBLEM, 'ผิดปกติ'),
    )

    student_id = models.AutoField(primary_key = True)
    key = models.CharField(max_length = 25, null = True)
    school = models.ForeignKey('main.School', on_delete = models.CASCADE, null = True)
    bus = models.ForeignKey('main.Bus', on_delete = models.CASCADE, null = True)
    status = models.CharField(max_length = 4, choices = STATUS_CHOICE, default= NORMAL, blank = True)
    bag_weight = models.IntegerField(blank = True, null = True) 

    def getName(self):
        return '{} {}'.format(self.getFirstName(),self.getLastName())
    def getBus(self):
        return self.bus.getBusNumber()
    def getBagWeight(self):
        return self.bag_weight
    def getStatus(self):
        return dict(self.STATUS_CHOICE).get(self.status)
    
class Teacher(Person):
    teacher_id = models.AutoField(primary_key = True)

class Parent(models.Model):
    user = models.OneToOneField('user.User', on_delete = models.CASCADE)
    phone = PhoneNumberField(null=False, blank=True, unique=True)
    student = models.ManyToManyField(Student)

class Admin(models.Model):
    user = models.OneToOneField('user.User', on_delete = models.CASCADE)
    test = models.CharField(max_length = 10, default = 'test', blank = True)
    school = models.OneToOneField('main.School', on_delete = models.CASCADE, null = True)
    #phone = PhoneNumberField(null=False, blank=True, unique=True)
    history = models.ForeignKey('main.History', on_delete = models.CASCADE, blank = True, null = True)
    