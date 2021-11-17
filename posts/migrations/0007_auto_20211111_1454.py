# Generated by Django 3.2.8 on 2021-11-11 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='OttType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='post',
            name='OttType',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='posts.OttType'),
        ),
    ]
