from django.db import models

#class Patient(models.Model):
#    first_names = models.CharField(max_length=100, verbose_name="First Names")
#    last_names  = models.CharField(max_length=100, verbose_name="Last Names")
#    id_card     = models.CharField(max_length=20, unique=True, verbose_name="ID Card")
#    birth_date  = models.DateField(verbose_name="Birth Date")
#    address     = models.CharField(max_length=150, verbose_name="Address")
#    phone       = models.CharField(max_length=20, verbose_name="Phone")
#    email       = models.EmailField(unique=True, verbose_name="Email")
#    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
#
#    def __str__(self):
#        return f"{self.first_names} {self.last_names}"
#
#    class Meta:
#        verbose_name = "Patient"
#        verbose_name_plural = "Patients"
from django.db import models
from django.conf import settings

class Patient(models.Model):
    first_names = models.CharField(max_length=100, verbose_name="Nombres")
    last_names  = models.CharField(max_length=100, verbose_name="Apellidos")
    id_card     = models.CharField(max_length=20, unique=True, verbose_name="Identificación")
    birth_date  = models.DateField(verbose_name="Fecha de cumpleaños")
    address     = models.CharField(max_length=150, verbose_name="Dirección")
    phone       = models.CharField(max_length=20, verbose_name="Teléfono")
    email       = models.EmailField(unique=True, verbose_name="Correo")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    created_by  = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patients_created",
        verbose_name="Created By",
        null=True,       # Permite nulos temporalmente
        blank=True
    )
    admins = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="patients_admin",
        verbose_name="Admins",
        help_text="All superusers associated with this patient."
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        # En la vista, asegúrate de asignar created_by al usuario logueado.
        super(Patient, self).save(*args, **kwargs)
        if is_new:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            superusers = User.objects.filter(is_superuser=True)
            self.admins.set(superusers)

    def __str__(self):
        return f"{self.first_names} {self.last_names}"

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
