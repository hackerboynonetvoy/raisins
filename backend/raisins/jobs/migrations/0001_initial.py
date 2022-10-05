# Generated by Django 4.1.1 on 2022-10-05 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=20000, null=True)),
                ('requirements', models.CharField(max_length=20000, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('street', models.CharField(max_length=255, null=True)),
                ('zip_code', models.CharField(max_length=128, null=True)),
                ('remote', models.BooleanField(null=True)),
                ('employment_type', models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time'), ('TM', 'Temporary'), ('CT', 'Contract'), ('IT', 'Internship'), ('SS', 'Seasonsal'), ('VT', 'Volunteer')], max_length=2, null=True)),
                ('category', models.CharField(choices=[('AT', 'Accounting'), ('AC', 'Administration and Clerical')], max_length=2, null=True)),
                ('education', models.CharField(choices=[('HC', 'High school coursework'), ('HS', 'High school or equivalent')], max_length=2, null=True)),
                ('experience', models.CharField(choices=[('HS', 'Student (High school)'), ('CL', 'Studnet (College)')], max_length=2, null=True)),
                ('min_hours', models.IntegerField(null=True)),
                ('max_hours', models.IntegerField(null=True)),
                ('min_salary', models.DecimalField(decimal_places=2, max_digits=16, null=True)),
                ('max_salary', models.DecimalField(decimal_places=2, max_digits=16, null=True)),
                ('resume', models.CharField(choices=[('R', 'Required'), ('O', 'Optional'), ('H', 'Hidden')], max_length=1, null=True)),
                ('cover_letter', models.CharField(choices=[('R', 'Required'), ('O', 'Optional'), ('H', 'Hidden')], max_length=1, null=True)),
                ('photo', models.CharField(choices=[('R', 'Required'), ('O', 'Optional'), ('H', 'Hidden')], max_length=1, null=True)),
                ('phone', models.CharField(choices=[('R', 'Required'), ('O', 'Optional'), ('H', 'Hidden')], max_length=1, null=True)),
                ('pipeline', models.JSONField(null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.department')),
                ('hiring_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hiring_manager', to=settings.AUTH_USER_MODEL)),
                ('recruiter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recruiter', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='jobs.tag')),
            ],
        ),
    ]
