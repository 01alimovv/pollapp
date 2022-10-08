from django.urls import path

from pollapp import views

app_name = 'pollapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

]

#mvt - model, views, template = django wula bn iwlid