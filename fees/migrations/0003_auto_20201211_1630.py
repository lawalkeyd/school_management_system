# Generated by Django 3.1 on 2020-12-11 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20201123_1545'),
        ('student', '0002_guardianinfo_login_details'),
        ('fees', '0002_auto_20201208_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfeespaid',
            name='fee_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='fees.fees'),
        ),
        migrations.AlterField(
            model_name='studentfees',
            name='fees',
            field=models.ManyToManyField(blank=True, to='fees.Fees'),
        ),
        migrations.AlterUniqueTogether(
            name='studentfees',
            unique_together={('student', 'session')},
        ),
    ]
