from django.urls import path
from . import views
from .views import natija

app_name = 'learn'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('natija/',natija.as_view(), name='natija'),
    path('exams/', views.ExamListView.as_view(), name='exams'),
    path('notes/', views.NotesListView.as_view(), name='notes'),

    path('mathematics/exams/<int:pk>/', views.MathExamView, name='math_exams'),
    # path('mathematics/notes/',),

    path('science/exams/<int:pk>/', views.ScienceExamsView, name='science_exams'),
    # path('science/notes/',),

]