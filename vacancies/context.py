from django.shortcuts import get_object_or_404

from vacancies.models import Vacancy


def get_current_user(request):
    return request.user if request.user.is_authenticated else None


def get_vacancy(vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    return vacancy
