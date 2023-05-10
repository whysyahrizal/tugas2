from django.shortcuts import render
from study_tracker.models import Assignment
from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from study_tracker.forms import AssignmentForm
from django.urls import reverse
from django.core import serializers

def show_tracker(request):
    assignment_data = Assignment.objects.all()
    context = {
        'list_of_assignment': assignment_data,
        'name': 'Wahyu Sahrijal'
    }

    return render(request, "tracker.html", context)


def create_assignment(request):
    form = AssignmentForm(request.POST or None)

    if form.is_valid():
        form.save()
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
