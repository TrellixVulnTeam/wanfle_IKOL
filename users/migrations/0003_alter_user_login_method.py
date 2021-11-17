# Generated by Django 3.2.8 on 2021-10-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_login_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login_method',
            field=models.CharField(blank=True, choices=[('email', 'Email'), ('kakao', 'Kakao')], default='email', max_length=7),
        ),
    ]
