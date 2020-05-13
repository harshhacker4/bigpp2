# Generated by Django 3.0.5 on 2020-05-04 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_delete_contact_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='supp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppico', models.CharField(max_length=500)),
                ('suppcol', models.CharField(default='#EF476F', max_length=15)),
                ('supptit', models.CharField(max_length=75)),
                ('suppdet', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'supps',
            },
        ),
    ]
