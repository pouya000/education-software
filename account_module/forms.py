from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ایمیل خود را وارد کنید'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'رمز خود را وارد کنید'}))
    repassword = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'رمز خود را مجددا وارد کنید'}))
    # def __str__(self):
    #     return self.email

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ایمیل خود را وارد کنید'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'رمز خود را وارد کنید'}))
    def __str__(self):
        return self.email