from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User


class Roles(models.Model):
    Role = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.Role)

class Course(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=1000)
    Creation_dae = models.DateTimeField(default=timezone.now)
    Photo = models.ImageField(upload_to='user_decorations', null=True, blank=True)
    Cost = models.IntegerField(null=True, blank=True)
    Owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='OwnerInCourse')
    Level = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return str(self.Name)


class CourseSection(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='Course')
    SectionName = models.CharField(max_length=200)
    SectionNumber = models.IntegerField()

    def __str__(self):
        return str(self.SectionName)


class CourseElementVideo(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='CourseInCourseElementLink')
    CourseSection = models.ForeignKey(CourseSection, on_delete=models.SET_NULL, null=True, blank=True, related_name='CourseSectionInCourseElementLink')
    Video = EmbedVideoField()
    Name = models.CharField(max_length=200, null=True, blank=True)


class CourseElementText(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='CourseInCourseElementText')
    CourseSection = models.ForeignKey(CourseSection, on_delete=models.SET_NULL, null=True, blank=True, related_name='CourseSectionInCourseElementText')
    Text = models.CharField(max_length=10000)
    Name = models.CharField(max_length=200, null=True, blank=True)


class UserDetail(models.Model):
    UserDetailUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='UserDetailUser')
    FOI = models.CharField(max_length=200)
    Mail = models.EmailField(null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Group = models.CharField(max_length=100, null=True, blank=True)
    Role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True, related_name='RoleInUserDetail')
    Avatar = models.ImageField(upload_to='users_profiles', null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Position = models.CharField(max_length=500, null=True, blank=True)
    Rating = models.IntegerField(null=True, blank=True)
    GraduatedPlace = models.CharField(max_length=300, null=True, blank=True)
    Status = models.CharField(max_length=700, null=True, blank=True)

    def __str__(self):
        return str(self.UserDetailUser.username)


class UserCourse(models.Model):
    UserInCourse = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='UserInUserCourse')
    Course = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='CourseInUserCourse')

class CourseElementQuiz(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='CourseInCourseElementQuiz')
    CourseSection = models.ForeignKey(CourseSection, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='CourseSectionInCourseElementQuiz')
    QuizText = models.CharField(max_length=500, blank=True, null=True)
    option1 = models.CharField(max_length=500, blank=True, null=True)
    option2 = models.CharField(max_length=500, blank=True, null=True)
    option3 = models.CharField(max_length=500, blank=True, null=True)
    option4 = models.CharField(max_length=500, blank=True, null=True)
    option1_answer = models.BooleanField(default=False)
    option2_answer = models.BooleanField(default=False)
    option3_answer = models.BooleanField(default=False)
    option4_answer = models.BooleanField(default=False)


class CourseSectionContent(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='CourseInSectionContent')
    CourseSection = models.ForeignKey(CourseSection, on_delete=models.SET_NULL, null=True, blank=True, related_name='CourseSectionInSectionContent')
    VideoType = models.ForeignKey(CourseElementVideo, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='CourseElementVideoInSectionContent')
    TextType = models.ForeignKey(CourseElementText, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='CourseElementTextInSectionContent')
    QuizType = models.ForeignKey(CourseElementQuiz, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='CourseElementQuizInSectionContent')
    CourseSectionContentType = models.CharField(max_length=100, null=True, blank=True)


class CourseAccess(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='CourseAccessCourse')
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='CourseAccessUser')
