# Generated by Django 4.0.4 on 2022-05-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsappli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('c_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('c_name', models.CharField(blank=True, max_length=35, null=True)),
                ('s_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'add_c',
            },
        ),
    ]
