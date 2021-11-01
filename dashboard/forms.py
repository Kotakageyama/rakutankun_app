from django import forms

class DownloadForm(forms.Form):
    prefix = forms.fields.ChoiceField(
        label='Prefix',required=True,widget=forms.widgets.Select
    )
    fromFrameNumber = forms.IntegerField(label='開始フレームナンバー')
    toFrameNumber = forms.IntegerField(label='終了フレームナンバー')

class DownloadCheckForm(forms.Form):
    prefix = forms.CharField(max_length=20,label='Prefix')
    fromFrameNumber = forms.IntegerField(label='開始フレームナンバー')
    toFrameNumber = forms.IntegerField(label='終了フレームナンバー')

class LoginForm(forms.Form):
    id = forms.CharField(label='学籍番号(s0000000)',max_length=20)
    passwd = forms.CharField(label='パスワード',max_length=20)
