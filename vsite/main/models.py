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

    ACTIVE = 'ACTV'
    STATION = 'STAY'
    ACCIDENT = 'ACCI'
    STATUS_CHOICE = (
        (ACTIVE, 'กำลังใช้งาน'), 
        (STATION, 'จอด'),
        (ACCIDENT, 'เกิดอุบัติเหตุ'),
    )
    STATUS_LABEL = (
        (ACTIVE, "background:#5cb75d;"), 
        (STATION, "background: #f0ad4e;"),
        (ACCIDENT, "background-color: #d9534f;"),
    )

    bus_id = models.AutoField(primary_key = True)
    bus_number = models.IntegerField(blank = True)
    status = models.CharField(max_length = 4, choices = STATUS_CHOICE, default= STATION, blank = True) 
    school = models.ForeignKey(School, on_delete = models.CASCADE, null = True)
    driver = models.ForeignKey('person.Driver', on_delete = models.CASCADE, null = True)
    
    current_speed = models.IntegerField(blank = True, default = 0)
    avg_speed = models.IntegerField(blank = True, default = 0)
    max_speed = models.IntegerField(blank = True, default = 0)
    
    def __str__(self):
        return str(self.bus_number)
    def getBusNumber(self):
        return self.bus_number
    def getStatus(self):
        return dict(self.STATUS_CHOICE).get(self.status)
    def getStatusLabel(self):
        return dict(self.STATUS_LABEL).get(self.status)
    def getDriverName(self):
        return self.driver.getName() if self.driver != None else '(no driver)'
    def getCurrentSpeed(self):
        return self.current_speed


class History(models.Model):

    #### const. for action #####
    GET_ON = 'ON'
    DEPART = 'DEP'
    GET_OFF = 'OFF'
    ACTION_CHOICES = (
        (GET_ON , 'Get_on'),
        (DEPART , 'Depart'),
        (GET_OFF , 'Get_off'),
    )
    ############################

    history_id = models.AutoField(primary_key = True)
    student = models.ForeignKey('person.Student', on_delete = models.CASCADE, null = True)
    bus = models.ForeignKey(Bus, on_delete = models.CASCADE, null = True)
    action = models.CharField(max_length = 3, choices = ACTION_CHOICES)
    time = models.DateTimeField(auto_now_add = True)
    location = models.ForeignKey(Location, on_delete = models.CASCADE, null = True)
