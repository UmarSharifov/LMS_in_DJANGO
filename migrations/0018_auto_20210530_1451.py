# Generated by Django 3.2.2 on 2021-05-30 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyschool', '0017_auto_20210520_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesectioncontent',
            name='QuizType',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CourseElementQuizInSectionContent', to='pyschool.courseelementtext'),
        ),
        migrations.CreateModel(
            name='CourseElementQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuizText', models.CharField(blank=True, max_length=500, null=True)),
                ('option1', models.CharField(blank=True, max_length=500, null=True)),
                ('option2', models.CharField(blank=True, max_length=500, null=True)),
                ('option3', models.CharField(blank=True, max_length=500, null=True)),
                ('option4', models.CharField(blank=True, max_length=500, null=True)),
                ('option1_answer', models.BooleanField(default=False)),
                ('option2_answer', models.BooleanField(default=False)),
                ('option3_answer', models.BooleanField(default=False)),
                ('option4_answer', models.BooleanField(default=False)),
                ('Course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CourseInCourseElementQuiz', to='pyschool.course')),
                ('CourseSection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CourseSectionInCourseElementQuiz', to='pyschool.coursesection')),
            ],
        ),
    ]
