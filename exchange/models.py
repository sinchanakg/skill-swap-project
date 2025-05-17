from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_offered = models.CharField(max_length=100)
    skill_needed = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} offers {self.skill_offered} for {self.skill_needed}"
