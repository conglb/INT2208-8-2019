# Generated by Django 2.1.7 on 2019-03-16 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(default='guest', max_length=25, primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=True)),
                ('is_restaurant', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, default='', null=True, verbose_name='last login')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(default='restaurant', max_length=25, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=True)),
                ('is_restaurant', models.BooleanField(default=False)),
                ('openTime', models.IntegerField(default=8)),
                ('closeTime', models.IntegerField(default=20)),
            ],
        ),
    ]