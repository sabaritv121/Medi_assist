from django import forms
from django.contrib.auth.forms import UserCreationForm

from Mediassist_app.models import Login_view, users, donor, Medicine_request, Medicine_approval


class DateInput(forms.DateInput):
    input_type = 'date'



class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login_view
        fields = ('username','password1','password2',)


class UsersRegister(forms.ModelForm):

    class Meta:
        model = users
        fields = "__all__"
        exclude = ("user",)


class DonorRegister(forms.ModelForm):

    class Meta:
        model = donor
        fields = "__all__"
        exclude = ("user",)



class MedicineForm(forms.ModelForm):

    end_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Medicine_request
        fields = "__all__"
        exclude = ('user','status_1')

class MedicineAprovalForm(forms.ModelForm):

    end_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Medicine_approval
        fields = "__all__"
