from django.shortcuts import render
from study_tracker.models import Assignment

def show_tracker(request):
    assignment_data = Assignment.objects.all()
    context = {
        'list_of_assignment': assignment_data,
        'name': 'Wahyu Sahrijal'
    }

    return render(request, "tracker.html", context)

