rom django.urls import path
from enroll import views

urlpatterns = [
    path('/', views.add_show, name="addandshow" )
]