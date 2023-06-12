from django.urls import path
from mysite.settings import MEDIA_URL
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),#1
    path('sighin/', views.signIn),#2
    path('postsignIn/', views.postsignIn),#3
    path('signUp/', views.signUp, name="signup"),#4
    path('logout/', views.logout, name="log"),#5
    path('postsignUp/', views.postsignUp),#6
    path('reset/', views.reset),#7
    path('postReset/', views.postReset),#8
    path('PostCreate/', views.PostCreate),#9
    path('Create/', views.Create),#10
    path('Home_page_admin/', views.Home_page_admin),#11
    path('Tela_sobre/', views.Tela_sobre),#12
    #path('search/', views.search),
    path('Add_autor/', views.Add_autor),#13
    path('Post_autor/', views.Post_autor),#14
    path('searchcontent/', views.searchcontent), #16
    path('PostDelete/', views.PostDelete), #17
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)