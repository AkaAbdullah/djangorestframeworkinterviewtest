from interviewtest import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('api/interviewList/',   views.interviewList.as_view()),
    path('public/api/interviewList/',   views.interviewListPublic.as_view()),

]
