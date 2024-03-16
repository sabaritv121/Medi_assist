from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login_view(AbstractUser):
    is_users = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)



class users(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE,related_name='users')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    blood_group = models.CharField(choices=BLOOD_GROUP_CHOICES,max_length=50)
    adhar_number = models.CharField(max_length=16)
    profile_pic = models.FileField(upload_to='profilepic/')

    def __str__(self):
        return self.name



class donor(models.Model):
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE,related_name='donor')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    reg_no = models.CharField(max_length=16)


    def __str__(self):
        return self.name



class Medicine_request(models.Model):

    CHOICE = [
        ('1-2 months', '1-2 months'),
        ('6 months', '6 months'),
        ('1 year', '1 year'),

    ]
    user = models.ForeignKey(Login_view, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now = True)
    end_date = models.DateField()
    medicine_name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50,choices=CHOICE)
    status_1 = models.IntegerField(default=0)


#
class Medicine_approval(models.Model):
    user = models.ForeignKey(donor,on_delete=models.CASCADE)
    approval = models.ForeignKey(Medicine_request, on_delete=models.CASCADE, related_name='approval')
    status1= models.IntegerField(default=0)
    status2 = models.IntegerField(default=0)