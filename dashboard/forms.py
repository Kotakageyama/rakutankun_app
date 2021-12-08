from django import forms

class LoginForm(forms.Form):
    student_id = forms.CharField(label='',max_length=20,
        widget=forms.TextInput(
            attrs={'placeholder':'学籍番号(12345678)', 'class':'form-control'}))
    passwd = forms.CharField(label='',max_length=20,
       widget=forms.TextInput(
            attrs={'placeholder':'パスワード', 'class':'form-control'}))
