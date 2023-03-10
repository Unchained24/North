# Generated by Django 4.1.5 on 2023-01-05 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
                ('account_balance', models.CharField(max_length=50)),
                ('account_pin', models.CharField(max_length=50)),
                ('dp', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='ItemImage')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
