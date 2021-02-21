from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from vacancies.context import get_current_user
from vacancies.forms import EditMyCompanyForm, EditMyVacancyForm
from vacancies.models import Company, Vacancy, Specialty


class UserCompanyCreate(View):

    def get(self, request):
        form = EditMyCompanyForm
        return render(request, 'vacancies/company-edit.html', {'form': form})

    def post(self, request):
        # Company.objects.create(
        #     name='Введите название компании',
        #     location='Введите местоположение компании',
        #     description='Введите описание компании',
        #     employee_count=1,
        #     logo=None,
        #     owner=request.user
        # )
        return redirect('/mycompany/')


class UserCompany(View):
    company_modify = False

    def get(self, request):
        user = get_current_user(request)
        if user is None:
            return redirect('/registration/login/')
        user_company = Company.objects.filter(owner=user).first()
        if user_company is None:
            return render(request, 'vacancies/company-create.html')
        else:
            form = EditMyCompanyForm(instance=user_company)
            return render(request, 'vacancies/company-edit.html', context={'user': user, 'form': form})

    def post(self, request):
        instance = get_object_or_404(Company, owner=request.user.id)
        form = EditMyCompanyForm(request.POST or None, instance=instance)
        user = get_current_user(request)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.owner = user
            post_form.save()
            self.company_modify = True
        context = {
            'form': form,
            'company_modify': self.company_modify}
        return render(request, 'vacancies/company-edit.html', context=context)


class UserCompanyVacancies(View):

    def get(self, request):
        user = get_current_user(request)
        if user is None:
            redirect('/login/')
        company = Company.objects.filter(owner=user).first()
        vacancies = Vacancy.objects.filter(company=company)
        context = {
            'vacancies': vacancies,
            'user': user,
        }
        return render(request, 'vacancies/vacancy-list.html', context=context)


class UserCompanyVacancy(View):
    vacancy_modify = False

    def get(self, request, vacancy_id):
        user = get_current_user(request)
        vacancy = Vacancy.objects.filter(pk=vacancy_id).first()
        if user is None:
            redirect('/login/')
        else:
            form = EditMyVacancyForm(instance=vacancy)
            context = {
                'vacancy': vacancy,
                'user': user,
                'form': form
            }
            return render(request, 'vacancies/vacancy-edit.html', context=context)

    def post(self, request, vacancy_id):
        user = request.user
        company = Company.objects.filter(owner=user).first()
        vacancy = Vacancy.objects.filter(id=vacancy_id).first()
        form = EditMyVacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            specialty = Specialty.objects.filter(id=vacancy.specialty).first()
            post_form = form.save(commit=False)
            post_form.specialty = specialty
            post_form.company = company
            post_form.save()
            self.vacancy_modify = True
        else:
            form = EditMyVacancyForm(instance=vacancy)
        context = {
            'form': form,
            'vacancy': vacancy,
            'vacancy_modify': self.vacancy_modify}
        return render(request, 'vacancies/vacancy-edit.html', context=context)
