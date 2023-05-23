from django.db import models

# Create your models here.

class Neighbor(models.Model):
    neighborName = models.CharField(max_length=45)
    neighborType = models.CharField(max_length=45)
    neighborBirthDay = models.DateTimeField()
    neighborAdded = models.DateTimeField(auto_now_add=True)
    neighborUpdated = models.DateTimeField(auto_now=True)

class Skill(models.Model):
    skillName = models.CharField(max_length=45)
    addedSkill = models.DateTimeField(auto_now_add=True)
    updatedSkill= models.DateTimeField(auto_now=True)