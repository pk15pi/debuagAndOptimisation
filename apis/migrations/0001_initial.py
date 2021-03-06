# Generated by Django 3.2.9 on 2021-11-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rank', models.CharField(max_length=25, null=True)),
                ('service', models.CharField(max_length=20, null=True)),
                ('experience', models.CharField(max_length=20, null=True)),
                ('qualification', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=10)),
                ('hrm_role', models.BooleanField(default=False)),
                ('scm_role', models.BooleanField(default=False)),
                ('operation_role', models.BooleanField(default=False)),
                ('project_role', models.BooleanField(default=False)),
                ('security_role', models.BooleanField(default=False)),
                ('admin_role', models.BooleanField(default=False)),
                ('it_role', models.BooleanField(default=False)),
                ('aviation_role', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=25)),
                ('course_name', models.CharField(max_length=100)),
                ('institute_name', models.CharField(max_length=100)),
                ('institute_location', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
