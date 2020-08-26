from django.urls import path

from . import views

app_name = 'category'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that displays all animals.
    path('animals/', views.animals, name='animals'),
    # Detail page for a single animal.
    path('animals/<int:animal_id>/', views.animal, name='animal'),
    # Page for adding a new animal.
    path('new_animal/', views.new_animal, name='new_animal'),
    #Page for adding a new description.
    path('new_description/<int:animal_id>/', views.new_description, name='new_description'),
    # Page for editing a description.
    path('edit_description/<int:description_id>/', views.edit_description, name='edit_description'),
]