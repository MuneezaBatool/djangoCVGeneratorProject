from django.db import models

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    summary = models.TextField(max_length=2000, null=True)

    skill1 = models.CharField(max_length=200, null=True)
    skill2 = models.CharField(max_length=200, null=True)
    skill3 = models.CharField(max_length=200, null=True)
    skill4 = models.CharField(max_length=200, null=True)

    degreeU = models.CharField(max_length=100, null=True)
    university = models.CharField(max_length=100, null=True)
    yearU = models.IntegerField(null=True)

    degreeC = models.CharField(max_length=100, null=True)
    college = models.CharField(max_length=100, null=True)
    yearC = models.IntegerField(null=True)

    degreeS = models.CharField(max_length=100, null=True)
    school = models.CharField(max_length=100, null=True)
    yearS = models.IntegerField(null=True)

    job_title1 = models.CharField(max_length=100, null=True)
    company1 = models.CharField(max_length=100, null=True)
    job_description1 = models.TextField(max_length=2000, null=True)
    start_date1 = models.DateField(null=True)
    end_date1 = models.DateField(null=True)

    job_title2 = models.CharField(max_length=100, null=True)
    company2 = models.CharField(max_length=100, null=True)
    job_description2 = models.TextField(max_length=2000, null=True)
    start_date2 = models.DateField(null=True)
    end_date2 = models.DateField(null=True)
