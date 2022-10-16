from django.urls import path
from django.contrib import admin
from .views import GeeksList
from .views import detail_view
from .views import update_view
from .views import delete_view
from .views import MyView
from .views import GeeksCreate
from .views import GeeksDetailView
from .views import GeeksUpdateView
from .views import GeeksDeleteView
from .views import GeeksFormView
#now import the views.py file into this code
from . import views
urlpatterns=[
  path('admin/', admin.site.urls),
  path('index/',views.index),
  path('home/',views.home_view),
  path('formset/',views.formset_view),
  path('Modelformset/',views.modelformset_view),
  path('geeks_view/', views.geeks_view),
  path('list_view/', views.list_view),
  path('geeksmodel_list/', GeeksList.as_view(template_name = "geeksmodel_list.html")),
  path('create_view/', views.create_view),
  path('<id>', detail_view ),
  path('update/<str:id>', update_view ),
  path('delete/<str:id>', delete_view ),
  path('about/', MyView.as_view()),
  path('', GeeksCreate.as_view(template_name = "geeksmodel_form.html") ),
  path('geeksmodel_detail/<pk>/', GeeksDetailView.as_view(template_name = "geeksmodel_detail.html")),
  path('updategeeks/<pk>/', GeeksUpdateView.as_view(template_name = "geeksmodel_form_2.html")),
  path('deletegeeks/<pk>/', GeeksDeleteView.as_view(template_name = "geeksmodel_confirm_delete.html")),
  path('formview/', GeeksFormView.as_view(template_name = "geeksmodel_form_3.html")),
  
]