from django.apps import AppConfig
from django.urls import path
from . import views


class AgiletimetableappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agiletimetableapp'

# yourappname/urls.py

urlpatterns = [
    path('', views.manage_subjects, name='manage_subjects'),
    path('edit_subject/<int:id>', views.edit_subject, name='edit_subject'),
    path('delete_subject/<int:id>', views.delete_subject, name='delete_subject'),
]
