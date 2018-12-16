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
    #score
    def getName(self):
        return self.getFirstName()

class Parent(models.Model):
    user = models.OneToOneField('user.User', on_delete = models.CASCADE)
    phone = PhoneNumberField(null=True, blank=True)

class Student(Person):
    
    IN_BUS = 'INBUS'
    DONTCARE = 'DNCARE'
    ARRIVE = 'ARRIVE'
    PROBLEM = 'PROB'
    STATUS_CHOICE = (
        (IN_BUS, 'อยู่ในรถ'), 
        (DONTCARE, 'กลับเอง'), 
        (ARRIVE, 'ถึงแล้ว'), 
        (PROBLEM, 'ผิดปกติ'),
    )
    STATUS_LABEL = (
        (IN_BUS, 'background:#5cb75d;'), 
        (DONTCARE, 'background: #f0ad4e;'), 
        (ARRIVE, 'background: #797979;'), 
        (PROBLEM, 'background-color: #d9534f;'),

    )

    student_id = models.AutoField(primary_key = True)
    location = models.ForeignKey('main.Location', on_delete = models.CASCADE, null = True)
    key = models.CharField(max_length = 25, null = True)
    school = models.ForeignKey('main.School', on_delete = models.CASCADE, null = True)
    bus = models.ForeignKey('main.Bus', on_delete = models.CASCADE, null = True)
    status = models.CharField(max_length = 6, choices = STATUS_CHOICE, default= DONTCARE, blank = True)
    
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, null = True)
    bag_weight = models.IntegerField(blank = True, null = True) 
    #weight 

    def getId(self):
        return self.student_id
    def getName(self):
        return '{} {}'.format(self.getFirstName(),self.getLastName())
    def getBus(self):
        return self.bus.getBusNumber()
    def getBagWeight(self):
        return self.bag_weight
    def getStatus(self):
        return dict(self.STATUS_CHOICE).get(self.status)
    def getStatusLabel(self):
        return dict(self.STATUS_LABEL).get(self.status)
    def getCurrentSpeed(self):
        return self.bus.getCurrentSpeed()

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
        return Student.objects.filter(school = self.school, status = Student.ARRIVE).count()
    def getInBusCount(self):
        return Student.objects.filter(school = self.school, status = Student.IN_BUS).count()
    def getStudentInSchool(self):
        return Student.objects.filter(school = self.school)