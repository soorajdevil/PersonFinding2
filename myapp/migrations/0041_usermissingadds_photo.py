# Generated by Django 4.2.6 on 2024-02-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_missing_found_pass_to_police'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermissingadds',
            name='Photo',
            field=models.ImageField(default='timezone.now()', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
