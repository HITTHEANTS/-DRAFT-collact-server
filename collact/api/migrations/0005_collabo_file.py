# Generated by Django 2.2.4 on 2019-11-14 10:31

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_change_url_to_file_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='collabo',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.Collabo.image_upload_path),
        ),
    ]