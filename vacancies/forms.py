from crispy_forms.helper import FormHelper
from django import forms

from vacancies.models import Application, Company, Vacancy, Specialty


class ApplicationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.field_class = 'col-lg-8'

    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter',)
        labels = {
            'written_username': 'Вас зовут',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо',
        }


class EditMyCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        TextAttrib = {'class': 'form-control', 'type': 'text'}
        fields = ('name', 'location', 'description', 'employee_count')
        widgets = {
            'name': forms.TextInput(attrs=TextAttrib),
            'location': forms.TextInput(attrs=TextAttrib),
            'description': forms.Textarea(attrs=TextAttrib),
            'employee_count': forms.NumberInput(attrs={'class': 'form-control'})
        }


class EditMyVacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        TextAttrib = {'class': 'form-control', 'type': 'text'}
        fields = ('title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max',)
        widgets = {
            'title': forms.TextInput(attrs=TextAttrib),
            'specialty': forms.Select(choices=Specialty.objects.all(), attrs=TextAttrib),
            'skills': forms.TextInput(attrs=TextAttrib),
            'description': forms.Textarea(attrs=TextAttrib),
            'salary_min': forms.NumberInput(attrs=TextAttrib),
            'salary_max': forms.NumberInput(attrs=TextAttrib),
        }
        labels = {'title': 'Название вакансии'}