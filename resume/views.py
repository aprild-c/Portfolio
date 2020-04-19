from django.shortcuts import render
from django import template
from resume.models import Experience, Course, Extracurricular, Skill

def convert(dates):
    for date in dates:
        date.month = 'Jan'
    return dates

def resume(request):
    experiences = Experience.objects.all()
    courses = Course.objects.all()
    extracurriculars = Extracurricular.objects.all()
    skills = Skill.objects.all().order_by('-level')

    context = {
        'experiences': experiences,
        'courses': courses,
        'extracurriculars': extracurriculars,
        'skills': skills,
    }
    return render(request, 'resume.html', context)

