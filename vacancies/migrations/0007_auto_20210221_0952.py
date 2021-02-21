# Generated by Django 3.1.6 on 2021-02-21 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0006_auto_20210221_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL),
        ),
    ]
