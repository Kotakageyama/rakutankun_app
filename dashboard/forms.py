from django import forms

class LoginForm(forms.Form):
    student_id = forms.CharField(label='学籍番号(12345678)',max_length=20)
    passwd = forms.CharField(label='パスワード',max_length=20)
