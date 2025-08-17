#from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):
    #return HttpResponse('<h1>Homepage</h1>')
    tasks= Task.objects.filter(is_completed=False).order_by('updated_at')
    context={
        'tasks':tasks,
    }
    return render(request,'home.html',context)