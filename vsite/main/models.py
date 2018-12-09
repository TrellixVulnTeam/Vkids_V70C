from django.db import models


# Create your models here.
class Location(models.Model):
    location_id = models.AutoField(primary_key = True)    
    street_address = models.CharField(max_length = 25)
    postal_code = models.CharField(max_length = 10)
    city = models.CharField(max_length = 30)
    state_province = models.CharField(max_length = 30)

class School(models.Model):
    school_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 40)
    location = models.OneToOneField(Location, on_delete = models.CASCADE, null = True)
    def __str__(self):
        return 'this school is : {}'.format(self.name)

class Bus(models.Model):
    bus_id = models.AutoField(primary_key = True)
    bus_number = models.IntegerField(blank = True)
    active = models.BooleanField(default = False) # false for not active, true for active 
    description = models.TextField(blank = True, null = True)
    school = models.ForeignKey(School, on_delete = models.CASCADE, null = True)
    driver = models.ForeignKey('person.Driver', on_delete = models.CASCADE, null = True)
    teacher = models.ForeignKey('person.Teacher', on_delete = models.CASCADE, null = True)
    
    def getBusNumber(self):
        return self.bus_number
    

    avg_speed = models.IntegerField(default = 0)
    max_speed = models.IntegerField(default = 0)

class History(models.Model):

    #### const. for action ######
    GET_ON = 'ON'
    DEPART = 'DEP'
    GET_OFF = 'OFF'
    ACTION_CHOICES = (
        (GET_ON , 'Get_on'),
        (DEPART , 'Depart'),
        (GET_OFF , 'Get_off'),
    )
    #############################

    history_id = models.AutoField(primary_key = True)
    student = models.ForeignKey('person.Student', on_delete = models.CASCADE, null = True)
    bus = models.ForeignKey(Bus, on_delete = models.CASCADE, null = True)
    action = models.CharField(max_length = 3, choices = ACTION_CHOICES)
    time = models.DateTimeField(auto_now_add = True)
    location = models.ForeignKey(Location, on_delete = models.CASCADE, null = True)
