# Generated by Django 4.2.5 on 2023-10-21 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_station1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital_Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('District', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Contact_number', models.IntegerField(null=True)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
