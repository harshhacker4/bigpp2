# Generated by Django 3.0.5 on 2020-05-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20200506_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
