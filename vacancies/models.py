from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    logo = models.URLField(default='https://place-hold.it/100x60', max_length=150)
    description = models.TextField(max_length=255)
    employee_count = models.IntegerField()

    def __str__(self):
        return f'{self.pk} {self.name}'


class Specialty(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    picture = models.URLField(default='https://place-hold.it/100x60', max_length=150)

    def __str__(self):
        return f'{self.pk} {self.title}'


class Vacancy(models.Model):
    title = models.CharField(max_length=150)
    specialty = models.ForeignKey(Specialty, related_name="vacancies", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="vacancies", on_delete=models.CASCADE)
    skills = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def __str__(self):
        return f'{self.pk} {self.company}'
