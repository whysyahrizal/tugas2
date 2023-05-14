from django.urls import path
from study_tracker.views import *

app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create_assignment/', create_assignment, name='create_assignment'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('update_assignment/<int:pk>/', update_assignment, name='update_assignment'),
    path('delete_assignment/<int:pk>/', delete_assignment, name='delete_assignment'),
    path('create-ajax/', create_assignment_ajax, name='create_assignment_ajax'),
    path('create-flutter/', create_assignment_flutter, name='create_assignment_flutter'),
]
