from django.db import models
from django.core.validators import EmailValidator, RegexValidator


class Customer(models.Model):
    name = models.CharField("Name:", max_length=300)
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.BigIntegerField("Phone Number:", default = '9876543210', validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    username = models.CharField("Username:", max_length=300)
    password = models.CharField("Password:", max_length=20)
    
    created = models.DateField(auto_now_add=True)

    



    def __str__(self):
        return self.name