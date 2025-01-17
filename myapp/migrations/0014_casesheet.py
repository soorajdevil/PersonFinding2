# Generated by Django 4.2.5 on 2023-12-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_rename_accident_accident1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casesheet',
            fields=[
                ('Patient_Name', models.CharField(max_length=100)),
                ('Blood_Group', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('District', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Contact_Number', models.CharField(max_length=100)),
                ('Age', models.IntegerField(primary_key=True, serialize=False)),
                ('Gender', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100)),
                ('Photo', models.FileField(upload_to='')),
                ('Patient_id', models.CharField(max_length=100)),
            ],
        ),
    ]
