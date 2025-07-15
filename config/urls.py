"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # admin side urls
    path('admin_login_view', views.admin_login_view, name='admin_login_view'),
    path('admin_logoutpage',views.admin_logout_view,name="admin_logoutpage"),
    path('admin_event_list',views.admin_event_list,name="admin_event_list"),
    path('add_event',views.add_event,name="add_event"),
    path('add_event_post',views.add_event_post,name="add_event_post"),
    path('delete_event/<int:id>/',views.delete_event,name="delete_event"),
    path('update_event/<int:id>/',views.update_event,name="update_event"),
    path('update_event_post/<int:id>/',views.update_event_post,name="update_event_post"),
    path('view_bookings/<int:id>/',views.view_bookings,name="view_bookings"),
    # user side urls
    path('',views.user_event_list,name="user_event_list"),
    path('user_book_event/<int:id>/',views.user_book_event,name="user_book_event"),
    path('book_event_post/<int:id>/',views.book_event_post,name="book_event_post"),
]
