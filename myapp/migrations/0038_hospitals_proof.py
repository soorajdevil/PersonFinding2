# Generated by Django 4.2.5 on 2024-01-27 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_missing_found_found_usermissing'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitals',
            name='proof',
            field=models.FileField(default='timezone.now()', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
