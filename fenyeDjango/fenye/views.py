from django.shortcuts import render,HttpResponse,redirect
from utils import pagination

# Create your views here.
LIST = []
for i in range(1, 509):
    LIST.append(i)
def user_list(request):
    current_page = request.GET.get('p',1)
    current_page = int(current_page)
    page_obj = pagination.Page(current_page,len(LIST))
    data = LIST[page_obj.start:page_obj.end]
    page_str = page_obj.page_str('/user_list/')
    return render(request,"user_list.html",{'page_str':page_str,'li':data})




###################COokie###################
user_info ={
    'hsj':{'pwd':'123123'},
}

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("pwd")
        dic = user_info.get(u)
        if not dic:
            return render(request,'login.html')
        if dic['pwd'] == p:
            res = redirect('/index/')
            res.set_cookie('username',u)
            return res
        else:
            return render(request, 'login.html')

def index(request):

    #获取当前已经登录的用户
    v = request.COOKIES.get("username")
    if not v:
        return redirect('/login/')
    return render(request,'index.html',{'current_user':v})