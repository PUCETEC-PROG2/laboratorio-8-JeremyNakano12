from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from pokedex.forms import PokemonForm
from .models import Pokemon, Trainer
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    template = loader.get_template('index.html')
    context = {
        'user': request.user,
        'logged_in': request.user.is_authenticated
    }
    return render(request, 'index.html', context)


def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(pk = pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, trainer_id):
    trainer = Trainer.objects.get(pk = trainer_id)
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
    return render(request, 'add_pokemon.html', {'form':form})
class CustomLoginView(LoginView):
    template_name = 'login.html'
