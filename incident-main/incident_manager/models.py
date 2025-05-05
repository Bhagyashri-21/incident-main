# incident_manager/models.py

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_mail = models.EmailField(max_length=254)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Incident(models.Model):
    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    brief_description = models.TextField()
    severity = models.CharField(max_length=50, choices=SEVERITY_CHOICES)
    attack_type = models.CharField(max_length=100)
    attack_vector = models.CharField(max_length=100)
    description = models.TextField()
    action_to_patch = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    security_researcher = models.CharField(max_length=100)

    def __str__(self):
        return self.title
