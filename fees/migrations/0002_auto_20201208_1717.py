# Generated by Django 3.1 on 2020-12-08 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fees',
            name='classes',
        ),
        migrations.AlterField(
            model_name='studentfees',
            name='paid',
            field=models.ManyToManyField(blank=True, to='fees.StudentFeesPaid'),
        ),
    ]
