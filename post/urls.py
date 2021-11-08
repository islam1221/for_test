from django.urls import path
from . import views

urlpatterns = [
   path('', views.blog_view),
   path('<int:id>/', views.blog_detail_view)
]