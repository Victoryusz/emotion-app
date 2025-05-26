from django.db import models
from django.utils import timezone

class DailyEntry(models.Model):
    MOOD_CHOICES = [
        ('feliz', 'Feliz'),
        ('triste', 'Triste'),
        ('ansioso', 'Ansioso'),
        ('calmo', 'Calmo'),
        ('irritado', 'Irritado'),
        ('grato', 'Grato'),
    ]

    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.mood} em {self.created_at}"
