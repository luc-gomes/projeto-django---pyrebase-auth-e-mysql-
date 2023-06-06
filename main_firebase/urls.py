from django.urls import path

from mysite.settings import MEDIA_URL
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    #path ("", views.index, name="index"),
    #path('', views.Main),
    path('sighin/', views.signIn),
    path('postsignIn/', views.postsignIn),
    path('signUp/', views.signUp, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),
    path('reset/', views.reset),
    path('postReset/', views.postReset),
    path('PostCreate/', views.PostCreate),
    path('Create/', views.Create),
    path('Home_page_admin/', views.Home_page_admin),
    path('', views.home),
    #when we are moving to search then move to this url
    #path('search/', views.search),
    #showing search detail on this url
    #path('searchcontent/', views.searchcontent),
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)