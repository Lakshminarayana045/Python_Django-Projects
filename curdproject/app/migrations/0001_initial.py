# Generated by Django 4.1.7 on 2023-04-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('gmail', models.EmailField(max_length=100)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]