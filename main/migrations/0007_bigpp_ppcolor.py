# Generated by Django 3.0.5 on 2020-05-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200504_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigpp',
            name='ppcolor',
            field=models.CharField(default='#EF476F', max_length=15),
        ),
    ]