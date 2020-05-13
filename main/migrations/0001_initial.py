# Generated by Django 3.0.5 on 2020-05-02 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ctitle', models.CharField(max_length=200)),
                ('Cdetails', models.CharField(max_length=200)),
                ('Cslug', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stitle', models.CharField(max_length=200)),
                ('Sdetails', models.CharField(max_length=200)),
                ('Category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.category', verbose_name='category')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('image', models.ImageField(default='https://images.unsplash.com/photo-1527683611643-4009f3a76197?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80', upload_to='images/')),
                ('slug', models.CharField(default=1, max_length=100)),
                ('Series', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.series', verbose_name='Series')),
            ],
            options={
                'verbose_name_plural': 'Skills',
            },
        ),
    ]