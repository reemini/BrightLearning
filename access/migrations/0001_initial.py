# Generated by Django 4.0.5 on 2022-06-05 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(blank=True, max_length=100)),
                ('Lesson', models.CharField(blank=True, max_length=200)),
                ('Note1', models.CharField(blank=True, max_length=500)),
                ('Note2', models.CharField(blank=True, max_length=500)),
                ('Note3', models.CharField(blank=True, max_length=500)),
                ('Note4', models.CharField(blank=True, max_length=500)),
                ('Note5', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]