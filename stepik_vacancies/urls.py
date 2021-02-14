"""stepik_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from vacancies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name='main'),
    path('vacancies/', views.VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:category>/', views.VacanciesByCategory.as_view(), name='vacancies_by_category'),
    path('companies/<int:company_id>/', views.CompanyView.as_view(), name='company'),
    path('vacancies/<int:vacancy_id>/', views.VacancyView.as_view(), name='vacancy'),
    path('__debug__/', include(debug_toolbar.urls)),
]

handler404 = views.custom_handler404
handler500 = views.custom_handler500
