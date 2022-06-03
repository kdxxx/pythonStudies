from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Parolayı doğrula",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data("username")
        password = self.cleaned_data("password")
        confirm = self.cleaned_data("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor")
        
        values = {
            "username" : username,
            "password" : password
        }
        return values
        