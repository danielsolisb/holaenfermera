from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, NurseProfile, SellerProfile, AccountAdminProfile, ClientProfile, Specialty
from .forms import CustomUserChangeForm, CustomUserCreationForm


class NurseProfileInline(admin.StackedInline):
    model = NurseProfile
    can_delete = False
    verbose_name_plural = 'Perfil Enfermero'

class SellerProfileInline(admin.StackedInline):
    model = SellerProfile
    can_delete = False
    verbose_name_plural = 'Perfil Vendedor'

class AccountAdminProfileInline(admin.StackedInline):
    model = AccountAdminProfile
    can_delete = False
    verbose_name_plural = 'Perfil Administrador Contable'

class ClientProfileInline(admin.StackedInline):
    model = ClientProfile
    can_delete = False
    verbose_name_plural = 'Perfil Cliente'

class CustomUserAdmin(BaseUserAdmin):
    # Configuración de campos y formularios, ya definida previamente
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('email', 'identification_number', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('identification_number', 'first_name', 'last_name', 'phone_number')}),
        ('Permisos', {'fields': ('user_type', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'identification_number', 'password1', 'password2', 'user_type'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name', 'identification_number')
    ordering = ('email',)

    def get_inline_instances(self, request, obj=None):
        inline_instances = []
        if obj:
            if obj.user_type == 'nurse':
                inline_instances.append(NurseProfileInline(self.model, self.admin_site))
            elif obj.user_type == 'seller':
                inline_instances.append(SellerProfileInline(self.model, self.admin_site))
            elif obj.user_type == 'account_admin':
                inline_instances.append(AccountAdminProfileInline(self.model, self.admin_site))
            elif obj.user_type == 'client':
                inline_instances.append(ClientProfileInline(self.model, self.admin_site))
        return inline_instances

admin.site.register(User, CustomUserAdmin)

class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Specialty, SpecialtyAdmin)


#from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth import get_user_model
#from .models import User
#from .forms import CustomUserChangeForm, CustomUserCreationForm
#class CustomUserAdmin(UserAdmin):
#    form = CustomUserChangeForm
#    add_form = CustomUserCreationForm
#    fieldsets = UserAdmin.fieldsets + (
#        (
#            None, {
#                'fields': (
#                    'id_ced',
#                    'address',
#                    'degree_title',
#                    'telephone',
#                    'country',
#                    #'company',
#                    'categorie',
#                    #'StationID',
#                )
#            }
#        ),
#    )
#
#class UserAdmin(CustomUserAdmin):
#    list_display =  (
#        'username',
#        'first_name',
#        'last_name',
#        'email',
#        'is_staff',
#        'is_active',
#        'is_superuser',
#        'id_ced',
#        'address',
#        'degree_title',
#        'telephone',
#        'country',
#        #'company',
#        'categorie',
#        'last_login',
#        'date_joined',
#    )
#
#
#
#admin.site.register(User, UserAdmin)