"""BucketList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from bucket import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', views.signupuser, name='signupuser' ),
    path('logout/', views.logoutuser, name='logoutuser' ),
    path('login/', views.loginuser, name='loginuser' ),
    #Bucket
    path('current/', views.currentbucket, name='currentbucket' ),
    path('create/', views.createbucket, name='createbucket' ),
    path('', views.home, name='home' ),
    path('bucket_item/<int:item_pk>', views.viewitem, name='viewitem' ),
    path('bucket_item/<int:item_pk>/complete', views.completeitem, name='completeitem' ),
    path('bucket_item/<int:item_pk>/delete', views.deleteitem, name='deleteitem' ),
    path('completed/', views.completedbucket, name='completedbucket' ),
]
