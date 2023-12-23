"""
URL configuration for biddingsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from biddingapp import views 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home ),
    path('register-vendor/', views.register_vendor),
    path('placebid/', views.placebid),
    # path('placebid/thanks/', views.placebid_thanks),
    path('viewbids/', views.view_bids),
    path('adminpanel/', views.adminpanel),
    path('login/', views.login),
    path('logout/', views.logout),
    path('support/', views.support),
    path('add-items/', views.add_items),
    path('list-items/', views.list_items),
    path('list-vendors/', views.list_vendors),
    path('bid-allotment/', views.bid_allotment),
    path('bid-results/', views.bid_results),
]
