# Generated by Django 4.0.4 on 2022-05-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsappli', '0002_coursedetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamDetails',
            fields=[
                ('s_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('s_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'add_s',
            },
        ),
    ]