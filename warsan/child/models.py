# child/models.py
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class Child(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    guardian = models.ForeignKey('Guardian', on_delete=models.CASCADE, related_name='children')
   
    def __str__(self):
        return f"{self.first_name} {self.last_name} (Child of {self.guardian})"


# guardian/models.py
from django.db import models
from child.models import Child  # Import Child model without issues

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    
)

class Guardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = PhoneNumberField(unique=True, region='IR')
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def register_child(self, first_name, last_name, date_of_birth, gender):
        child = Child.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            guardian=self,
        )
        return child

    def get_children(self):
        return self.children.all()
