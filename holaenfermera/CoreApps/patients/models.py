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
    # Se cambia el nombre y el significado del campo ManyToMany para reflejar que puede asociarse a cualquier usuario.
    related_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="patients_related",
        verbose_name="Related Users",
        help_text="Users associated with this patient."
    )

    def save(self, *args, **kwargs):
        # No se realiza asignación automática; la relación se gestionará manualmente o a través de formularios.
        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_names} {self.last_names}"

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"