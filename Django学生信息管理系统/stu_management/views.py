from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from stu_management.models import Student
from stu_management import models
# Create your views here.

def login(requset):
    if requset.method =='POST':
        u = requset.POST.get('UserName',None)
        p = requset.POST.get('password',None)
        if u == 'hsj' and p =='1111':
            return redirect('/home/')

    return render(requset,'login.html')


def home(requset):

    print(requset.method)
    if requset.method =='POST':
        name = requset.POST.get('name',None)
        stu_ID = requset.POST.get('stu_ID',None)
        gender = requset.POST.get('gender',None)
        class_stu = requset.POST.get('class_stu',None)
        seat = requset.POST.get('seat',None)
        course = requset.POST.get('course',None)
        score = requset.POST.get('score',None)
        status = requset.POST.get('status',None)
        models.Student.objects.create( name=name,
                                       stu_ID=stu_ID,
                                       gender = gender,
                                       class_stu = class_stu,
                                       seat = seat,
                                       course = course,
                                       score = score,
                                       status = status,)
    student_date = Student.objects.all()

    # student = Student.objects.all()[0].name
    # print(student)
    return render(requset,'home.html',{'student_date':student_date})


def user_del(request,nid):
    print(nid)
    models.Student.objects.filter(id = nid).delete()
    return redirect('/home/')
def user_detail(request,nid):
    obj = models.Student.objects.filter(id=nid).first()
    print(obj.id)
    return render(request,'userdetial.html',{'obj':obj})