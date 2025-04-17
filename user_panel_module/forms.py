from django import forms
from account_module.models import User



class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels= {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'تصویر پروفایل',
        }

    # name = forms.CharField(label='نام',
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'})
    # )
    # family = forms.CharField(label='نام خانوادگی',
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'})
    # )
    # avatar = forms.FileField(label='تصویر آواتار',
    #     # widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تصویر آواتار'})
    # )