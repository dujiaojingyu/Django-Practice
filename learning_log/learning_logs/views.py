from django.shortcuts import render
from .models import Topic
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse 此导入方式在Django已经改变
from django.urls import reverse
from .forms import TopicForm
# Create your views here.
def index(request):
    '''学习笔记的主页'''
    return render(request,'learning_logs/index.html')

def topics(request):
    '''显示所有主题'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request,topic_id):
    '''显示所有主题'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    '''添加主题'''
    if request.method != 'POST':
        #未提交数据：创建一个新表单
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)