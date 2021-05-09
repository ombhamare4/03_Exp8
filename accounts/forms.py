from django.forms import ModelForm
from .models import UsersAccounts

class CreateUserLogForm(ModelForm):
    class Meta:
        model=UsersAccounts
        fields=['username','email','password']