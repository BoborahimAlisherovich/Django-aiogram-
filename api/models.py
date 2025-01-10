from django.db import models

# Create your models here.

class BotUser(models.Model):
    user_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120,null=True,blank=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Feedback(models.Model):
    user_id = models.CharField(max_length=120,null=True,blank=True)
    create_at = models.DateField(auto_now_add=True)
    body = models.CharField(max_length=120,null=True,blank=True)
    def __str__(self):
        return f"{self.body}"
    


