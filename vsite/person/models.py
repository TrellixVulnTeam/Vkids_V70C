from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    phone = PhoneNumberField(null=False, blank=True, unique=True)
    age = models.IntegerField(null=True, blank=True)

class Driver(Person):
    driver_id = models.AutoField(primary_key = True)

class Student(Person):
    student_id = models.AutoField(primary_key = True)
    key = models.CharField(max_length = 25, null = True)
    bus = models.ForeignKey('main.Bus', on_delete = models.CASCADE, null = True)
    
class Teacher(Person):
    teacher_id = models.AutoField(primary_key = True)



class Parent(models.Model):
    user = models.OneToOneField('user.User', on_delete = models.CASCADE)
    phone = PhoneNumberField(null=False, blank=True, unique=True)
    student = models.ManyToManyField(Student)

class Admin(models.Model):
    user = models.OneToOneField('user.User', on_delete = models.CASCADE)
    phone = PhoneNumberField(null=False, blank=True, unique=True)
    history = models.ForeignKey('main.History', on_delete = models.CASCADE, null = models.CASCADE)