from django.conf.urls import url
from second_app import views
from django.urls import path, include
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView , LogoutView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'second_app'

urlpatterns = [
    url(r'^logout/',views.logout,name="log"),
    url(r'^signIn/$',views.signIn,name='signIn'),
    url(r'^$',views.index,name='index'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^postsign/',views.postsign,name = 'postsign'),
    url(r'^FAQ/',views.FAQ,name='FAQ'),
    url(r'^Postsignup/',views.postsignup,name='postsignup'),
    url(r'^Resources/',views.resources,name='resources'),
    url(r'^Registration/',views.registration,name='registration'),
    url(r'^mission/',views.mission,name='mission'),
    url(r'^signin/',views.signin,name='signin'),
    path('$/postsign/', views.postsign,name='postsign'),
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('',views.indexView,name="home"),
    path('Apply/',views.apply,name='apply'),

    #path('login/',views.redirect_view,name="login_url")








]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
