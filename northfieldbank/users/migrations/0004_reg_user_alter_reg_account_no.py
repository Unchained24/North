# Generated by Django 4.1.5 on 2023-01-19 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_reg_country_reg_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='reg',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reg',
            name='account_no',
            field=models.CharField(max_length=50, null='TRUE'),
        ),
    ]
