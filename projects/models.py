from django.db import models

#set blank and null attr with helper function
def nullable_field(field_class, *args, **kwargs):
    kwargs['blank'] = True
    kwargs['null'] = True
    return field_class(*args, **kwargs)


# Create your models here.
class Project(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=250)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    links = nullable_field(models.URLField, max_length=300)
    image = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk}. {self.title}"


class AboutEducation(models.Model):
    campus = nullable_field(models.CharField, max_length=100)
    field = nullable_field(models.CharField ,max_length=50)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    relevant_courses = nullable_field(models.CharField, max_length=800)

    def __str__(self):
        return f"{self.pk}. {self.campus}"


class AboutExperience(models.Model):
    organization = nullable_field(models.CharField, max_length=100)
    job_title = nullable_field(models.CharField, max_length=100)
    location = nullable_field(models.CharField, max_length=100)
    start_date = nullable_field(models.DateField)
    end_date = nullable_field(models.DateField)
    job_description = nullable_field(models.TextField)
    notes = nullable_field(models.CharField, max_length=200)

    def __str__(self):
        return f"{self.pk}. {self.organization}"


class AboutSkills(models.Model):
    skill = nullable_field(models.CharField, max_length=50)
    description = nullable_field(models.TextField)

    def __str__(self):
        return f"{self.pk}. {self.skill}"


class AboutLanguages(models.Model):
    languages = nullable_field(models.CharField, max_length=100)

    def __str__(self):
        return f"{self.pk}. {self.languages} "
    

class AboutInterests(models.Model):
    interests = nullable_field(models.CharField, max_length=100)

    def __str__(self):
        return f"{self.pk}. {self.interests} "