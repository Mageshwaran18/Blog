from django.urls import path
from .import views
from .views import custom_logout


urlpatterns = [
    path('logout/', custom_logout, name='logout'),
    path('profile/',views.profile,name = 'profile'),
    path('profile/profile_update/',views.profile_update,name = 'profile_update'),
    path('logoutt/', views.logout_form, name='logoutt'),
]