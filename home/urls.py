from django.urls import path

from home import views


urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('sections/', views.Sections.as_view())
]