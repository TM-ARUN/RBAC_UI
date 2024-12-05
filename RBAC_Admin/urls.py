"""
URL configuration for RBAC_Admin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from admin_dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard1/',views.user_management_view),
    path('user1/',views.users),
    path('add_user/',views.add_user),
    path('edit_user/<int:id>',views.edit_user),
    path('edit_user2/<int:id>',views.edit_user2),
    path('delete_user/<int:id>',views.delete_user),
    path('rolemanage/',views.role_manager),
    path('add_role/',views.add_role),
    path('delete_role/<int:id>',views.delete_role),
    path('edit_role/<int:id>',views.edit_role),
    path('edit_role2/<int:id>',views.edit_role2),
    path('permissionmanage/',views.permission_manager),
    path('add_permission/',views.add_permission),
    path('edit_permission/<int:id>',views.edit_permission),
    path('edit_permission2/<int:id>',views.edit_permission2),
    path('delete_permission/<int:id>',views.delete_permission),
]
