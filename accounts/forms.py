from django import forms

from .models import User


class UserCreationForm(forms.ModelForm):
    # password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        print(user.password)
        user.save()
        return user