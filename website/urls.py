from django.urls import path
from . import views
from django.urls import re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('add/addissue/', views.addissue, name='addissue'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/editline/<int:id>', views.editline, name='editline'),
    path('delete/<int:id>', views.delete, name='delete'),
    re_path(r'^.*$', RedirectView.as_view(url='http://localhost:8000/', permanent=False), name='index'),
]
