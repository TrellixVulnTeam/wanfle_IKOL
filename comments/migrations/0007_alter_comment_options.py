# Generated by Django 3.2.8 on 2021-11-11 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
    ]
