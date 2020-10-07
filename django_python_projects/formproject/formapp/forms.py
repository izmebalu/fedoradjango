from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    college = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput)
    gpa = forms.IntegerField()
    address = forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])

#    def clean_name(self):
#        inputname = self.cleaned_data['name']
#        print("Valid name")
#        if len(inputname)<4:
#        return inputname
    def clean(self):
        print("Total form validation")
        cleaned_data = super().clean()
        inputname = cleaned_data['name']
        if len(inputname) < 2:
            raise forms.ValidationError("This is less than 5 characters")
        inputroll = cleaned_data['rollno']
        if len(str(inputroll)) < 3:
            raise forms.ValidationError("SHould be more than 3 digits")
        inputpassword = cleaned_data['password']
        inputrpassword = cleaned_data['rpassword']
        if inputpassword != inputrpassword:
            raise forms.ValidationError("Passwords not matched")
