from django import forms

class LoginForm(forms.Form):
    student_id = forms.CharField(label='',max_length=20,
        widget=forms.TextInput(
            attrs={'placeholder':'学籍番号(12345678)', 'class':'form-control'}))
    passwd = forms.CharField(label='',max_length=20,
       widget=forms.TextInput(
            attrs={'placeholder':'パスワード', 'class':'form-control'}))

    # student_id = forms.CharField(label='学籍番号',max_length=20)
    # passwd = forms.CharField(label='パスワード',max_length=20)

class ProfileDataForm(forms.Form):
    student_id = forms.CharField(label="学籍番号(12345678)",max_length=20)
    passwd = forms.CharField(label='パスワード',max_length=20)
    # user_credits
    # credits_list

class UserUpdateForm(forms.Form):
    student_id = forms.CharField(label="学籍番号(12345678)",max_length=20)
    passwd = forms.CharField(label='パスワード',max_length=20)
    choicelist = forms.MultipleChoiceField(
        label='科目選択',
        required=False,
        disabled=False,
        widget=forms.CheckboxSelectMultiple(attrs={
            'id': 'choicelist','class': 'form-check-input'}))