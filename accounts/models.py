from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        CLIENT = 'CLIENT', 'MSME Client'
        AGENT = 'AGENT', 'UEH Support Agent'
        ADMIN = 'ADMIN', 'UEH Admin'

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.CLIENT)
    business_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    @property
    def is_client(self):
        return self.role == self.Role.CLIENT

    @property
    def is_agent(self):
        return self.role == self.Role.AGENT

    @property
    def is_ueh_admin(self):
        return self.role == self.Role.ADMIN

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'