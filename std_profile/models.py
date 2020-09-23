
from django.db import models
from django_countries.fields import CountryField
from address.models import AddressField


Gender=(
    ('fem', 'Female'),
    ('ma', 'Male'),
)


class Profile(models.Model):
    Image = models.ImageField(upload_to='img/',null=True, blank=True)
    First_name = models.CharField(max_length=50)
    Last_name= models.CharField(max_length=50)
    Student_id = models.AutoField(primary_key=True)
    Date_of_birth = models.DateField(auto_now=False)
    Current_age = models.IntegerField()
    Gender = models.CharField(choices=Gender, max_length=50)
    State = CountryField()
    City_street =AddressField()
    Postal_code = models.IntegerField()
    Email = models.EmailField(max_length=254)
    Telephone_number = models.IntegerField()
    Mother_tongue= models.CharField(max_length=50)
    Payment_method= models.CharField(max_length=50)



class ProfileImg(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='img/',null=True, blank=True)





















