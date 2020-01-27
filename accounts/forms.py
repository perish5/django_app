from django.contrib.auth.forms import UserCreationForm #UserCreationForm  creates user form
from django import forms
from accounts.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username") # we can use __all__ also for all fields


# it is used to check the email is valid,unique or not
# yo process hamle views.py mani garna milxa tara views ma check garda tya database ma import huni hunale tyo error cost expensive hunxa
    def clean_email(self):
            data = self.cleaned_data["email"]
            try:
                user_email = User.objects.get(email=data)
            except User.DoesNotExist:
                pass
                #return data
            else:
                raise forms.ValidationError("Email already exist")

    def clean_contact_no(self):
        data = self.cleaned_data["contact_no"]
        for i in data:
            if not (i.isdigit() or i in "+-"):
                raise forms.ValidationError("Invalid contact number")