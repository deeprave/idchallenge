from django.urls import path, register_converter
from api import views
from api import converters

register_converter(converters.PkConverter, 'pk')

urlpatterns = [

  path('gender/<pk:pk>/', views.GenderDetail.as_view()),
  path('gender/', views.GenderList.as_view()),

  path('age/<pk:pk>/', views.AgeDetail.as_view()),
  path('age/', views.AgeList.as_view()),

  path('state/<pk:pk>/', views.StateDetail.as_view()),
  path('state/', views.StateList.as_view()),

  path('regiontype/<pk:pk>/', views.RegionTypeDetail.as_view()),
  path('regiontype/', views.RegionTypeList.as_view()),

  path('region/<pk:pk>/', views.RegionDetail.as_view()),
  path('region/', views.RegionList.as_view()),

  path('year/<pk:pk>/', views.YearDetail.as_view()),
  path('year/', views.YearList.as_view()),

  path('statistic/<pk:pk>/', views.StatisticDetail.as_view()),
  path('statistic/', views.StatisticList.as_view()),

]
