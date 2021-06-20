from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *

def index(request):
    Courses = Course.objects.all()
    return render(request, 'index.html', context={
        'courses': Courses,
    })

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            role = Roles.objects.get(Role='Пользователь')
            temp = UserDetail(UserDetailUser=request.user, Role=role)
            temp.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

def profile(request):
    user = request.user
    user_detail = UserDetail.objects.get(UserDetailUser=request.user)
    courses = CourseAccess.objects.filter(User=user)
    return render(request, 'profile.html', context={
        'user': user,
        'user_detail': user_detail,
        'courses': courses,
    })


def profile_change(request):
    user = request.user
    user_detail = UserDetail.objects.get(UserDetailUser=request.user)
    form = ChangeProfileUser(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            user_detail.FOI = form.cleaned_data['FOI']
            user_detail.Mail = form.cleaned_data['Mail']
            user_detail.Phone = form.cleaned_data['Phone']
            user_detail.Group = form.cleaned_data['Group']
            user_detail.Country = form.cleaned_data['Country']
            user_detail.GraduatedPlace = form.cleaned_data['GraduatedPlace']
            user_detail.Status = form.cleaned_data['Status']
            user_detail.Avatar = form.cleaned_data['Avatar']
            user_detail.save()
            return render(request, 'profile.html', context={
                'user': user,
                'user_detail': user_detail,
            })
        else:
            return redirect('/')
    form = ChangeProfileUser()
    return render(request, 'profile_change.html', context={
        'user': user,
        'user_detail': user_detail,
        'form': form,
    })


def about(request):
    return render(request, 'about.html')


def courses(request):
    Courses = Course.objects.all()
    return render(request, 'Courses.html', context={
        'courses': Courses,
    })

def course_create(request):
    user = request.user
    user_detail = UserDetail.objects.get(UserDetailUser=request.user)
    form = CourseCreateForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            course = Course.objects.create(
                Name=form.cleaned_data['Name'],
                Description=form.cleaned_data['Description'],
                Photo=form.cleaned_data['Photo'],
                Owner=request.user,
                Level=form.cleaned_data['Level'],
                                           )
            course.save()
            acces = CourseAccess.objects.update_or_create(
                Course=course,
                User=request.user
            )
            return render(request, 'profile.html', context={
                'user': user,
                'user_detail': user_detail,
            })
        else:
            return redirect('/')
    form = CourseCreateForm()
    return render(request, 'course_create.html', context={
        'user': user,
        'user_detail': user_detail,
        'form': form,
    })


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    user = request.user
    sections = CourseSection.objects.filter(Course=course)
    course_section_content = CourseSectionContent.objects.filter(Course=course)
    return render(request, 'course_detail.html', context= {
        'course': course,
        'current_user':user,
        'sections': sections,
        'course_section_content': course_section_content,
    })


def addTextInCourse(request,course_id, section_id):
    form = CourseElementTextForm(request.POST)
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            temp1 = CourseElementText.objects.create(
                Course=Course.objects.get(id=course_id),
                CourseSection=CourseSection.objects.get(id=section_id),
                Text=form.cleaned_data['content'],
                Name=form.cleaned_data['Name'])
            temp1.save()
            temp = CourseSectionContent.objects.create(
                Course=Course.objects.get(id=course_id),
                CourseSection=CourseSection.objects.get(id=section_id),
                VideoType=None,
                TextType=temp1,
                QuizType=None,
                CourseSectionContentType='1')
            temp.save()
            course = Course.objects.get(id=course_id)
            course_sections = CourseSection.objects.get(id=section_id)
            course_section_content = CourseSectionContent.objects.filter(Course=course)
            return redirect('course_detail', course_id=course_id)
        else:
            form = CourseElementTextForm()
            return render(request, 'addTextInCourse.html', context={
                'form': form,

            })
    form = CourseElementTextForm()
    return render(request, 'addTextInCourse.html', context={
        'form': form,
    })

def course_element_learning(request, course_id, element_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        user = request.user
        sections = CourseSection.objects.filter(Course=course)
        course_section_content = CourseSectionContent.objects.filter(Course=course)
        current_content = CourseSectionContent.objects.get(id=element_id)
        # if (current_content.QuizType.option1_answer == request.POST.get['option1']):
        question_numbers = request.POST.getlist('options')
        print(question_numbers)
        answer = False
        counter = 0
        for i in question_numbers:
            if ((i == '1') and (current_content.QuizType.option1_answer == True)
            or (i == '2') and (current_content.QuizType.option2_answer == True)
            or (i == '3') and (current_content.QuizType.option3_answer == True)
            or ((i == '4') and (current_content.QuizType.option4_answer == True))
            ):
                answer = True
            else:
                answer = False
        return render(request, 'course_element_learning.html', context={
            'course': course,
            'current_user': user,
            'sections': sections,
            'course_section_content': course_section_content,
            'current_content': current_content,
            'answer': answer,
        })
    else:
        course = Course.objects.get(id=course_id)
        user = request.user
        sections = CourseSection.objects.filter(Course=course)
        course_section_content = CourseSectionContent.objects.filter(Course=course)
        current_content = CourseSectionContent.objects.get(id=element_id)
        return render(request, 'course_element_learning.html', context= {
            'course': course,
            'current_user':user,
            'sections': sections,
            'course_section_content': course_section_content,
            'current_content': current_content,
        })

def addVideoInCourse(request,course_id, section_id):
    form = CourseElementVideoForm(request.POST)
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            temp1 = CourseElementVideo.objects.create(
                Course=Course.objects.get(id=course_id),
                CourseSection=CourseSection.objects.get(id=section_id),
                Video=form.cleaned_data['Video'],
                Name=form.cleaned_data['Name'])
            temp1.save()
            temp = CourseSectionContent.objects.create(
                Course=Course.objects.get(id=course_id),
                CourseSection=CourseSection.objects.get(id=section_id),
                VideoType=temp1,
                TextType=None,
                QuizType=None,
                CourseSectionContentType='2')
            temp.save()
            course = Course.objects.get(id=course_id)
            return redirect('course_detail', course_id=course_id)
        else:
            form = CourseElementVideoForm()
            return render(request, 'addVideoInCourse.html', context={
                'form': form,
            })
    form = CourseElementVideoForm()
    return render(request, 'addVideoInCourse.html', context={
        'form': form,
    })


def addQuizInCourse(request,course_id, section_id):
    form = CourseElementQuizForm(request.POST)
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            temp1 = CourseElementQuiz.objects.create(
                Course=Course.objects.get(id=course_id),
                CourseSection=CourseSection.objects.get(id=section_id),
                QuizText=form.cleaned_data['QuizText'],
                option1=form.cleaned_data['option1'],
                option2=form.cleaned_data['option2'],
                option3=form.cleaned_data['option3'],
                option4=form.cleaned_data['option4'],
                option1_answer=form.cleaned_data['option1_answer'],
                option2_answer=form.cleaned_data['option2_answer'],
                option3_answer=form.cleaned_data['option3_answer'],
                option4_answer=form.cleaned_data['option4_answer'],
            )
            temp1.save()
            temp = CourseSectionContent.objects.create(
                Course=Course.objects.get(id=course_id),
                CourseSection=CourseSection.objects.get(id=section_id),
                VideoType=None,
                TextType=None,
                QuizType=temp1,
                CourseSectionContentType='3')
            temp.save()
            course = Course.objects.get(id=course_id)
            course_sections = CourseSection.objects.get(id=section_id)
            course_section_content = CourseSectionContent.objects.filter(Course=course)
            return redirect('course_detail', course_id=course_id)
        else:
            form = CourseElementQuizForm()
            return render(request, 'addQuizInCourse.html', context={
                'form': form,

            })
    form = CourseElementQuizForm()
    return render(request, 'addQuizInCourse.html', context={
        'form': form,
    })


def course_confirm(request, course_id):
    course = Course.objects.get(id=course_id)
    acces = CourseAccess.objects.update_or_create(
        Course=course,
        User=request.user
    )
    return render(request, 'course_confirm.html')