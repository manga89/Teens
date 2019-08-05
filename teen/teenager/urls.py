from django.urls import path

from .views import HomePageView, StudentCreateView, StudentDetailView, StudentListView,StudentUpdateView

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('create/', StudentCreateView.as_view(), name ='student_create' ),
path('all/', StudentListView.as_view(), name='all_teens'),
path('<pk>/detail', StudentDetailView.as_view(), name="teen_detail"),
path('<pk>/update/', StudentUpdateView.as_view(), name="update_teen"),
]
