# Generated by Django 3.1 on 2020-11-23 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highest_education', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=45, null=True)),
                ('board', models.CharField(max_length=45)),
                ('passing_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeJobInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('account', 'Account'), ('hostel', 'Hostel'), ('security', 'Security'), ('admin', 'Administration'), ('others', 'Others')], max_length=45)),
                ('joning_date', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.department')),
                ('job_designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.designation')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('former_job', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('place', models.CharField(max_length=100)),
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
                ('nationality', models.CharField(max_length=45)),
                ('religion', models.CharField(max_length=45)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('driving_license_passport', models.IntegerField(unique=True)),
                ('phone_no', models.CharField(max_length=11, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('father_name', models.CharField(max_length=45)),
                ('mother_name', models.CharField(max_length=45)),
                ('marital_status', models.CharField(choices=[('married', 'Married'), ('widowed', 'Widowed'), ('separated', 'Separated'), ('divorced', 'Divorced'), ('single', 'Single')], max_length=10)),
                ('education', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.educationinfo')),
                ('experience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.experienceinfo')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employeejobinfo')),
                ('training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.traininginfo')),
            ],
        ),
    ]
