from django.conf import settings
from django.db import models


class Opportunity(models.Model):
    class Kind(models.TextChoices):
        FUNDING = 'FUNDING', 'Funding'
        TENDER = 'TENDER', 'Tender'
        TRAINING = 'TRAINING', 'Training'

    title = models.CharField(max_length=200)
    kind = models.CharField(max_length=10, choices=Kind.choices)
    description = models.TextField()
    closing_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['closing_date']
        verbose_name_plural = 'opportunities'

    def __str__(self):
        return self.title


class Application(models.Model):
    class Status(models.TextChoices):
        SUBMITTED = 'SUBMITTED', 'Submitted'
        APPROVED = 'APPROVED', 'Approved'
        REJECTED = 'REJECTED', 'Rejected'

    opportunity = models.ForeignKey(
        Opportunity, on_delete=models.CASCADE, related_name='applications'
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications'
    )
    motivation = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.SUBMITTED)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('opportunity', 'client')

    def __str__(self):
        return f'{self.client} -> {self.opportunity}'