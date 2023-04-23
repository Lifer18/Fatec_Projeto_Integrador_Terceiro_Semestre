# Generated by Django 4.1.7 on 2023-04-21 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='name')),
                ('birthday', models.PositiveIntegerField(default=0, null=True, verbose_name='birthday')),
                ('nationality', models.CharField(max_length=200, verbose_name='nationality')),
                ('username', models.CharField(max_length=200, verbose_name='username')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
            ],
        ),
    ]
