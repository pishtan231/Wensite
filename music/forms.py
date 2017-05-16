from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
from website.settings import PASSWORD_HASHERS

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'PASSOWRD...','title': 'Sh...'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder': 'USER NAME', 'title': 'User Name'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'placeholder': 'YOUR EMAIL...', 'title': 'xxx@mailService.yyyy'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    prefixEncrypt = 'django.contrib.auth.hashers.'


    CHOICES = (
        ((PASSWORD_HASHERS[0][len(prefixEncrypt):]).strip(), 'PBKDF2'),
        ((PASSWORD_HASHERS[1][len(prefixEncrypt):]).strip(), 'PBK2SHA1'),
        ((PASSWORD_HASHERS[2][len(prefixEncrypt):]).strip(), 'SHA1'),
        ((PASSWORD_HASHERS[3][len(prefixEncrypt):]).strip(), 'MD5'),
)

    encrypt = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = UserProfile
        fields = ('encrypt', )



class EmailForm(forms.Form):

    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)