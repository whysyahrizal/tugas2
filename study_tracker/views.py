from django.shortcuts import render, redirect
from study_tracker.models import Assignment
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from study_tracker.forms import AssignmentForm
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='/study_tracker/login/')
def show_tracker(request):
    # restriction for user
    list_of_assignment = Assignment.objects.filter(user=request.user)
    total_assignment = list_of_assignment.count()
    form = AssignmentForm()  # Tambahkan ini
    context = {
        'list_of_assignment': list_of_assignment,
        'name' : request.user.username,
        'total_assignment' : total_assignment,
        'last_login': request.COOKIES['last_login'],
        'form': form,  # Tambahkan ini
    }

    return render(request, "tracker.html", context)

@csrf_exempt
def create_assignment_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_assignment = Assignment.objects.create(
            user=request.user,
            name = data["name"],
            subject = data["subject"],
            progress = int(data["progress"]),
            date=datetime.datetime.now(),
            description = data["description"]
        )

        new_assignment.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:   
            login(request, user)
            response = HttpResponseRedirect(reverse('study_tracker:show_tracker'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('study_tracker:show_tracker'))
    response.delete_cookie('last_login') 
    return response

def create_assignment(request):
   form = AssignmentForm(request.POST or None)

   if form.is_valid():
      new_assignment = form.save(commit=False)
      new_assignment.user = request.user
      new_assignment.save()
      return HttpResponseRedirect(reverse('study_tracker:show_tracker'))

   context = {'form': form}
   return render(request, 'form_create_assignment.html', context)

    

def show_xml(request):
    data = Assignment.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Assignment.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Assignment.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Assignment.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def update_assignment(request, pk):
    assignment = Assignment.objects.get(id=pk)
    form = AssignmentForm(instance=assignment)

    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('study_tracker:show_tracker'))

    context = {'form': form}
    return render(request, 'form_update_assignment.html', context)

def delete_assignment(request, pk):
    assignment = Assignment.objects.get(id=pk)
    assignment.delete()
    return HttpResponseRedirect(reverse('study_tracker:show_tracker'))

from django.http import JsonResponse

def create_assignment_ajax(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.user = request.user
            assignment.save()
            response_data = {
                'result': 'success',
                'assignment': {
                    'id': assignment.id,
                    'name': assignment.name,
                    'subject': assignment.subject,
                    'progress': assignment.progress,
                    'date': assignment.date,
                    'description': assignment.description
                }
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'result': 'error'})
    else:
        return JsonResponse({'result': 'error'})

def register(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Akun telah berhasil dibuat!')
            return redirect('study_tracker:show_tracker')
        
    context = {'form': form}
    return render(request, 'register.html',  context) 
