# Generated by Django 4.1.2 on 2023-07-04 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('middle_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('nation', models.CharField(max_length=15)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_passport', to='users.user')),
            ],
        ),
    ]