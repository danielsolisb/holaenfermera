from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from .models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'
        widgets = {
            'user_type': forms.Select(choices=User.USER_TYPE_CHOICES),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Puedes incluir aquí otros campos si lo requieres (por ejemplo, first_name y last_name)
        fields = ('email', 'user_type', 'phone_number')

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # Para el registro de clientes, se puede forzar en la vista que user_type sea "client"
        fields = ["email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        # Actualizamos los campos a los que realmente disponemos en el nuevo modelo
        fields = ['first_name', 'last_name', 'phone_number']


#from django.contrib.auth.forms import UserChangeForm, UserCreationForm
#from django.db.models.base import Model
#from django.forms import ModelForm
#from django import forms
#
#from .models import User
#
#
#class CustomUserChangeForm(UserChangeForm):
#    class Meta(UserChangeForm.Meta):
#        model = User
#        fields = '__all__'
#        widgets = {
#            'categorie': forms.Select(choices=User.options),
#        }
#
#
#class CustomUserCreationForm(UserCreationForm):
#    class Meta(UserCreationForm.Meta):
#        model = User
#
#class UserProfileForm(ModelForm):
#    pass
#
#class RegisterForm(UserCreationForm):
#    email = forms.EmailField()
#
#    class Meta:
#        model = User
#        fields = ["username", "email", "password1", "password2"]
#    
#    
#
#class UserUpdateForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ['first_name', 'last_name', 'id_ced', 'address', 'telephone', 'country']
#    #def __init__(self, *args, **kwargs):
#    #    super().__init__(*args, **kwargs)
#    #    self.helper = FormHelper(self)
#    #    self.helper.form_method = 'post'
#    #    self.helper.add_input(Submit('submit', 'Save'))