from django.contrib import admin
from django.urls import path,include
from pdf import views 
from authen import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accept', views.accept, name="accept"),
    path('', views.firstPage, name="firstPage"),
    path('resume/<int:id>/',views.resume, name="resume"),
    path('list/',views.list, name="list"),
    #authentication urls
    path('register/', user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='authen/login.html'),name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='authen/logout.html'),name='logout'),
    path('profile/', user_views.profilepage, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



