from django.db import models

# Create your models here.

# class disease(models.Model):
#     description = models.TextField()
#     symptoms = models.TextField()
#     treatment = models.TextField()

class symptoms(models.Model):
    gender = models.TextField()
    age = models.TextField()
    pas_no_trat = models.TextField()
    pas_trat = models.TextField()
    diabetes = models.TextField()
    smoking_status = models.TextField()
    ecv = models.TextField()
    fa = models.TextField()
    hvi = models.TextField()

class expertreponse(models.Model):
    id_disease = models.TextField()
    description = models.TextField()
    treatment = models.TextField()
