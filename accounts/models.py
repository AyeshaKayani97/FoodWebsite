from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from django.dispatch import Signal
# from django.core.validators import RegexValidator
# Create your models here.
# phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
#                                 message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class Profile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE )
    # phone_number = models.CharField(max_length=17,validators=[phone_regex],unique=True)
    is_email_verified = models.BooleanField(default=False)
    otp = models.IntegerField(null=True, blank=True)
    profile_image=models.ImageField(upload_to="profile", null=True, blank=True)


    # def create_user_profile
