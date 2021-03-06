# Generated by Django 2.2.2 on 2019-09-22 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Company_Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail'), ('Not-Attended', 'Not-Attended')], default='Not-Attended', max_length=30)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company_Round')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Company_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Registered', 'Registered'), ('Rejected', 'Rejected'), ('Not-Registered', 'Not-Registered')], default='Not-Registered', max_length=30)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
