from django.db import models
from django.contrib.auth.models import User

# Optional: If you want to extend the User model with extra fields
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, choices=[
        ('Accounts', 'Accounts'),
        ('HR', 'HR'),
        ('IT', 'IT'),
        ('Marketing', 'Marketing')
    ])
    
    def __str__(self):
        return f"{self.user.username} - {self.department}"
