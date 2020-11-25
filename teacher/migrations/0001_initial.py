# Generated by Django 3.1 on 2020-11-23 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
        ('academic', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=255)),
                ('group', models.CharField(choices=[('university', 'University'), ('polythenic', 'Polythenic'), ('college', 'College')], max_length=100)),
                ('grade', models.CharField(max_length=45)),
                ('nysc_information', models.CharField(max_length=45)),
                ('graduation_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('former_job', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=45)),
                ('trainer', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('assistant', 'Assistant Teacher'), ('subject teacher', 'Subject Teacher'), ('class teacher', 'Class Teacher'), ('other', 'Others')], max_length=45)),
                ('joining_date', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.department')),
                ('job_designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.designation')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(max_length=100, null=True)),
                ('year', models.IntegerField(null=True)),
                ('duration', models.IntegerField(null=True)),
                ('place', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('photo', models.ImageField(upload_to='')),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=45)),
                ('nationality', models.CharField(choices=[('Nigerian', 'Nigerian'), ('Others', 'Others')], max_length=45)),
                ('religion', models.CharField(choices=[('Christianity', 'Christianity'), ('Islam', 'Islam'), ('Others', 'Others')], max_length=45)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('blood_group', models.CharField(choices=[('a+', 'A+'), ('o+', 'O+'), ('b+', 'B+'), ('ab+', 'AB+'), ('a-', 'A-'), ('o-', 'O-'), ('b-', 'B-'), ('ab-', 'AB-')], max_length=5)),
                ('driving_license_passport', models.IntegerField(unique=True)),
                ('phone_no', models.CharField(max_length=11, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('father_name', models.CharField(max_length=45)),
                ('mother_name', models.CharField(max_length=45)),
                ('marital_status', models.CharField(choices=[('married', 'Married'), ('widowed', 'Widowed'), ('separated', 'Separated'), ('divorced', 'Divorced'), ('single', 'Single')], max_length=10)),
                ('is_delete', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('education', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.educationinfo')),
                ('experience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.experienceinfo')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.jobinfo')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.traininginfo')),
            ],
        ),
    ]
