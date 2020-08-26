from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Animal, Description
from .forms import AnimalForm, DescriptionForm

def index(request):
    """The home page for Animal World."""
    return render(request, 'category/index.html')

@login_required    
def animals(request):
    """Shows all animals"""
    animals = Animal.objects.filter(owner=request.user).order_by('date_added')
    context = {'animals': animals}
    return render(request, 'category/animals.html', context)

@login_required    
def animal(request, animal_id):
    """Show a single animal and all its descriptions"""
    animal = get_object_or_404(Topic, id=animal_id)
    # Make sure the animal belongs to the current user.
    if animal.owner != request.user:
        raise Http404
        
    descriptions = animal.description_set.order_by('-date_added')
    context = {'animal': animal, 'descriptions': descriptions}
    return render(request, 'category/animal.html', context)
    
@login_required
def new_animal(request):
    """Add a new animal."""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = AnimalForm()
    else:
        #POST data submitted; process data.
        form = AnimalForm(data=request.POST)
        if form.is_valid():
            new_animal = form.save(commit=False)
            new_animal.owner = request.user
            new_animal.save()
            return redirect('category:animals')
            
    # Display a blank or invalid form.
    context ={'form': form}
    return render(request, 'category/new_animal.html', context)
    

@login_required    
def new_description(request, animal_id):
    """Add a new description for a particular animal."""
    animal = Animal.objects.get(id=animal_id)
        
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = DescriptionForm()
    else:
        # POST data submitted; process data.
        form = DescriptionForm(data=request.POST)
        if form.is_valid():
            new_description = form.save(commit=False)
            new_description.animal = animal
            new_description.save()
            return redirect('category:animal', animal_id=animal_id)
                
    # Display a blank or invalid form.
    context = {'animal': animal, 'form': form}
    return render(request, 'category/new_description.html', context)
    

@login_required   
def edit_description(request, description_id):
    """Edit an existing description."""
    description = Description.objects.get(id=description_id)
    animal = description.animal
    if animal.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current description.
        form = DescriptionForm(instance=description)
    else:
        # POST data submitted; process data.
        form = DescriptionForm(instance=description, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('category:animal', animal_id=animal.id)
            
    context = {'description': description, 'animal': animal, 'form': form}
    return render(request, 'category/edit_description.html', context)
