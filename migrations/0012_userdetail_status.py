# Generated by Django 3.2.2 on 2021-05-16 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyschool', '0011_userdetail_graduatedplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='Status',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
    ]
