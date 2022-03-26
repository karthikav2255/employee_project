"""employees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from owner import views
from django.conf.urls.static import static
from django.conf import settings
from customer import views as cv
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/owner/add', views.EmployeeView.as_view(),name='addemployee'),
    path('employee/owner/all',views.EmployeeListView.as_view(),name='employeelist'),
    path('employee/<int:id>',views.EmployeeDetailView.as_view(),name='employeedetail'),
    path('employee/remove/<int:id>',views.EmployeeDeleteView.as_view(),name='employeedelete'),
    path('employee/change/<int:id>',views.EmployeeChangeDetailsView.as_view(),name='employeeedit'),
    path('customer/',include("customer.urls"))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
