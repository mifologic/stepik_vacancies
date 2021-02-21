from datetime import datetime

from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from vacancies.context import get_current_user, get_vacancy
from vacancies.forms import ApplicationForm, EditMyCompanyForm, EditMyVacancyForm
from vacancies.models import Specialty, Vacancy, Company, Application


class MainView(View):

    def get(self, request):
        specialties = Specialty.objects.all().annotate(count=Count('vacancies'))
        company_vacancies = Company.objects.all().annotate(count=Count('vacancies'))
        context = {
            'specialties': specialties,
            'company_vacancies': company_vacancies,
        }
        return render(request, 'vacancies/index.html', context=context)


class VacanciesByCategory(View):

    def get(self, request, category):
        specialty = get_object_or_404(Specialty, code=category)
        vacancies = Vacancy.objects.filter(specialty=specialty)
        context = {
            'vacancies': vacancies,
            'specialty': specialty,
        }
        return render(request, 'vacancies/vacancies.html', context=context)


class VacanciesView(View):

    def get(self, request):
        vacancies = Vacancy.objects.all()
        context = {
            'vacancies': vacancies,
        }
        return render(request, 'vacancies/vacancies.html', context=context)


class SendView(View):
    template_name = 'vacancies/send.html'

    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        return render(
            request, self.template_name,
            context={
                'vacancy': vacancy,
            }
        )


class VacancyView(View):

    def get(self, request, vacancy_id):
        vacancy = get_vacancy(vacancy_id)
        form = ApplicationForm
        context = {
            'vacancy': vacancy,
            'form': form,
        }
        return render(request, 'vacancies/vacancy.html', context=context)

    def post(self, request, vacancy_id):
        form = ApplicationForm(request.POST)
        user = get_current_user(request)
        vacancy = get_vacancy(vacancy_id)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = user
            application.vacancy = vacancy
            application.save()
            return redirect('send', vacancy_id)
        return render(request, 'vacancies/vacancy.html', {'form': form})


class CompanyView(View):

    def get(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        vacancy = get_object_or_404(Vacancy, company=company_id)
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
