# Generated by Django 2.2.2 on 2019-09-22 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_company_round',
            old_name='company',
            new_name='company_round',
        ),
    ]
