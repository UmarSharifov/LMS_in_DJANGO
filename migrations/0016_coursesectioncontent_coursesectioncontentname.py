# Generated by Django 3.2.2 on 2021-05-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyschool', '0015_coursesectioncontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesectioncontent',
            name='CourseSectionContentName',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
