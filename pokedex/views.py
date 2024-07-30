from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from pokedex.forms import PokemonForm, TrainerForm
from .models import Pokemon, Trainer
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

def index(request):
    template = loader.get_template('index.html')
    context = {
        'user': request.user,
        'logged_in': request.user.is_authenticated
    }
    return render(request, 'index.html', context)


def pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk = trainer_id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

def list_pokemon(request):
    pokemons = Pokemon.objects.order_by('type')
    template = loader.get_template('list_pokemon.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def list_trainer(request):
    trainers = Trainer.objects.order_by('region')
    template = loader.get_template('list_trainer.html')
    return HttpResponse(template.render({'trainers': trainers}, request))

@login_required
def add_pokemon(request):
    if request.method =='POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:list_pokemon')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form':form})

@login_required
def add_trainer(request):
    if request.method =='POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:list_trainer')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form':form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk = pokemon_id) 
    if request.method =='POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:list_pokemon')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form':form})

@login_required
def edit_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk = trainer_id) 
    if request.method =='POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:list_trainer')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form':form})

@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk = pokemon_id)
    pokemon.delete()
    return redirect("pokedex:list_pokemon")

@login_required
def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk = trainer_id)
    trainer.delete()
    return redirect("pokedex:list_trainer")