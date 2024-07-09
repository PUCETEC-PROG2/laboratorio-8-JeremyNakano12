from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer

def index(request):
    with open('pokedex/templates/index.html', 'r') as index:
        indexhtml = index.read()
    return HttpResponse(indexhtml)


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