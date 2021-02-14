from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

from vacancies.models import Specialty, Vacancy, Company


class MainView(View):
    model = Specialty, Company

    def get(self, request):
        specialties = Specialty.objects.all().annotate(count=Count('vacancies'))
        company_vacancies = Company.objects.all().annotate(count=Count('vacancies'))
        context = {
            'specialties': specialties,
            'company_vacancies': company_vacancies,
        }
        return render(request, 'vacancies/index.html', context=context)


class VacanciesByCategory(View):
    model = Vacancy

    def get(self, request, category):
        specialty = Specialty.objects.get(code=category)
        vacancies = Vacancy.objects.filter(specialty=specialty)
        context = {
            'vacancies': vacancies,
            'specialty': specialty,
        }
        return render(request, 'vacancies/vacancies.html', context=context)


class VacanciesView(View):
    model = Vacancy

    def get(self, request):
        vacancies = Vacancy.objects.all()
        context = {
            'vacancies': vacancies,
        }
        return render(request, 'vacancies/vacancies.html', context=context)


class VacancyView(View):
    model = Vacancy

    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(pk=vacancy_id)
        company = Company.objects.filter(pk=vacancy.company.id)
        context = {
            'vacancy': vacancy,
            'company': company,
        }
        return render(request, 'vacancies/vacancy.html', context=context)


class CompanyView(View):
    model = Company

    def get(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        vacancy = Vacancy.objects.get(company=company_id)
        vacancies_count = Vacancy.objects.filter(company__id=company_id).count()
        context = {
            'company': company,
            'vacancy': vacancy,
            'vacancies_count': vacancies_count,
        }
        return render(request, 'vacancies/company.html', context=context)


def custom_handler404(request, exception):
    """
    :return: Возвращает сообщение, если запрашиваемая страница не найдена.
    """
    return HttpResponseNotFound('Страница не найдена. Зайдите попозже.')


def custom_handler500(request):
    """
    :return: Возвращает сообщение, если сервер недоступен.
    """
    return HttpResponseServerError('Сервер недоступен. Зайдите попозже.')
