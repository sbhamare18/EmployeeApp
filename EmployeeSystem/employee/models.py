from django.db import models

# Create your models here.
# Employee Model to create table in db
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emp_id = models.AutoField(primary_key=True)
    emp_salary = models.FloatField()
    #default image will be 'profilepic.jpg' and image will vbe uploaded to 'profile_pictures'
    emp_profile_picture = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    phone_number = models.CharField(max_length=20)
    address = models.TextField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name