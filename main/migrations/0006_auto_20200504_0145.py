# Generated by Django 3.0.5 on 2020-05-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200504_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigpp',
            name='ppicon',
            field=models.CharField(max_length=500),
        ),
    ]