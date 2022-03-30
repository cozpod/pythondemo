"""themePro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from jet_django.urls import jet_urls
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('themeApp.urls')),
    # path(r'^jet_api/', include('jet_django.urls')),
    path('jet_api/', include('jet_django.urls')),
    # path(r'^jet_api/', include('jet_urls.urls')),


#  path('products/<int:pk>/$', views.ProductDetailView.as_view(), name='details')

]