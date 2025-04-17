from django import forms


class make_quiz_form(forms.Form):
    question1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'سوال اول را وارد کنید؟ '}))
    q1_a = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه اول را وارد کنید: ..................... '}))
    q1_b = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه دوم را وارد کنید: ..................... '}))
    q1_c = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه سوم را وارد کنید: ..................... '}))
    q1_d = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه چهارم را وارد کنید: ..................... '}))
    question2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'سوال دوم را وارد کنید؟ '}))
    q2_a = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه اول را وارد کنید: '}))
    q2_b = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه دوم را وارد کنید: '}))
    q2_c = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه سوم را وارد کنید: '}))
    q2_d = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه چهارم را وارد کنید: '}))
    question3 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'سوال سوم را وارد کنید؟'}))
    q3_a = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه اول را وارد کنید: '}))
    q3_b = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه دوم را وارد کنید: '}))
    q3_c = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه سوم را وارد کنید: '}))
    q3_d = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه چهارم را وارد کنید: '}))
    question4 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'سوال چهارم را وارد کنید؟ '}))
    q4_a = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه اول را وارد کنید: '}))
    q4_b = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه دوم را وارد کنید: '}))
    q4_c = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه سوم را وارد کنید: '}))
    q4_d = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه چهارم را وارد کنید: '}))

class student_quiz_form(forms.Form):
    question = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'سوال را وارد کنید: '}))
    options1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه اول را وارد کنید: '}))
    options2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه دوم را وارد کنید: '}))
    options3 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه سوم را وارد کنید: '}))
    options4 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'گزینه چهارم را وارد کنید: '}))

