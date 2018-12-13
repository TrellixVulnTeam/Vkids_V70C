from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from main.models import Bus

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    phone = PhoneNumberField(null=True, blank=True)
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
    
    NORMAL = 'NORMAL'
    IN_BUS = 'INBUS'
    OUT_BUS = 'OUTBUS'
    PROBLEM = 'PROBLM'
    STATUS_CHOICE = (
        (NORMAL, 'ปกติ'), 
        (IN_BUS, 'อยู่ในรถ'), 
        (OUT_BUS, 'ลงรถ'), 
        (PROBLEM, 'ผิดปกติ'),
    )

    student_id = models.AutoField(primary_key = True)
    location = models.ForeignKey('main.Location', on_delete = models.CASCADE, null = True)
    key = models.CharField(max_length = 25, null = True)
    school = models.ForeignKey('main.School', on_delete = models.CASCADE, null = True)
    bus = models.ForeignKey('main.Bus', on_delete = models.CASCADE, null = True)
    status = models.CharField(max_length = 6, choices = STATUS_CHOICE, default= NORMAL, blank = True)
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
    phone = PhoneNumberField(null=True, blank=True)
    student = models.ManyToManyField(Student, blank = True)

class Admin(models.Model):
    user = models.OneToOneField('user.User', on_delete = models.CASCADE)
    school = models.OneToOneField('main.School', on_delete = models.CASCADE,blank = True, null = True)
    phone = PhoneNumberField(null=True, blank=True)
    history = models.ForeignKey('main.History', on_delete = models.CASCADE, blank = True, null = True)

    def getSchool(self):
        return self.school
    def getBusActive(self):
        return Bus.objects.filter(school = self.school, status = Bus.ACTIVE).count()
    def getBusStation(self):
        return Bus.objects.filter(school = self.school, status = Bus.STATION).count()
    def getOutBusCount(self):
        return Student.objects.filter(school = self.school, status = Student.OUT_BUS).count()
    def getInBusCount(self):
        return Student.objects.filter(school = self.school, status = Student.IN_BUS).count()
    def getStudentInSchool(self):
        return Student.objects.filter(school = self.school)