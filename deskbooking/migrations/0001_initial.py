# Generated by Django 4.1.7 on 2023-04-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk_name', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('employee_reserved_name', models.CharField(max_length=200)),
            ],
        ),
    ]
