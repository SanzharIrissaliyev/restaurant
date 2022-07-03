# Generated by Django 4.0.5 on 2022-07-03 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mini_title', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='upload')),
                ('instagram', models.CharField(max_length=300)),
                ('facebook', models.CharField(max_length=300)),
                ('twitter', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='upload')),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('peoples', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='upload')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='upload')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]
