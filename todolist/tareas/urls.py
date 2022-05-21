from django.urls import path
from .views import TareasListView

urlpatterns = [   
    path('',TareasListView.as_view(), name='listado'),  
]