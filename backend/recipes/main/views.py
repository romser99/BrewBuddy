from math import exp
import random
from django import urls
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipe
from .forms import *
from.formset import *
from django.db import transaction
from django.contrib.auth import login, authenticate, logout
from django.db.models import Count, Q
from django.core.paginator import Paginator


def main(request):
    top_10_recipes = Recipe.objects.annotate(like_count=Count('Likes')).order_by('-like_count')[:10]
    if len(top_10_recipes) < 3:
        random_recipes = top_10_recipes
    else:
        random_recipes = random.sample(list(top_10_recipes), 3)
    context = {'recipes': random_recipes, 'user': request.user}
    return render(request, 'index.html', context)


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
        
    else:
        form = LoginForm(request)
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main')

@login_required
def check_stock_malt(request):
    malts = StockMalt.objects.filter(user=request.user)

    if request.method == 'POST':
        form = AddMaltForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('malt_inventory')
        form = AddMaltForm()

    context = {'malts' : malts}
    return render(request, 'malt_inventory.html', context)

@login_required
def check_stock_hop(request):
    hops = StockHop.objects.filter(user=request.user)

    if request.method == 'POST':
        form = AddHopForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('hop_inventory')
    else:
        form = AddHopForm()
    
    context = {'hops' : hops}
    return render(request, 'hop_inventory.html', context)



@login_required
def check_stock_yeast(request):
    yeasts = StockYeast.objects.filter(user=request.user)

    if request.method == 'POST':
        form = AddYeastForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('yeast_inventory')
    else:
        form = AddYeastForm()

    context = {'yeasts' : yeasts}
    return render(request, 'yeast_inventory.html', context)

@login_required
def check_stock_extra(request):
    extras = StockExtra.objects.filter(user=request.user)

    if request.method == 'POST':
        form = AddExtraForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('extra_inventory')
    else:
        form = AddExtraForm()

    context = {'extras' : extras}
    return render(request, 'extra_inventory.html', context)

@login_required
def remove_malt(request, malt_id):
    malt = get_object_or_404(StockMalt, pk=malt_id, user=request.user)
    malt.delete()
    return redirect('malt_inventory')

@login_required
def remove_hop(request, hop_id):
    hop = get_object_or_404(StockHop, pk=hop_id, user=request.user)
    hop.delete()
    return redirect('hop_inventory')

@login_required
def remove_yeast(request, yeast_id):
    yeast = get_object_or_404(StockYeast, pk=yeast_id, user=request.user)
    yeast.delete()
    return redirect('yeast_inventory')

@login_required
def remove_extra(request, extra_id):
    extra = get_object_or_404(StockExtra, pk=extra_id, user=request.user)
    extra.delete()
    return redirect('extra_inventory')

@login_required
def edit_malt(request, malt_id):
    malt = get_object_or_404(StockMalt, pk=malt_id, user=request.user)
    if request.method == 'POST':
        form = AddMaltForm(request.POST, instance=malt)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('malt_inventory')
    else:
        form = AddMaltForm(instance=malt)
    return render(request, 'edit_malt.html', {'form': form})

@login_required
def edit_hop(request, hop_id):
    hop = get_object_or_404(StockHop, pk=hop_id, user=request.user)
    if request.method == 'POST':
        form = AddHopForm(request.POST, instance=hop)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('hop_inventory')
    else:
        form = AddHopForm(instance=hop)
    return render(request, 'edit_hop.html', {'form': form})

@login_required
def edit_yeast(request, yeast_id):
    yeast = get_object_or_404(StockYeast, pk=yeast_id, user=request.user)
    if request.method == 'POST':
        form = AddYeastForm(request.POST, instance=yeast)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('yeast_inventory')
    else:
        form = AddYeastForm(instance=yeast)
    return render(request, 'edit_yeast.html', {'form': form})

@login_required
def edit_extra(request, extra_id):
    extra = get_object_or_404(StockExtra, pk=extra_id, user=request.user)
    if request.method == 'POST':
        form = AddExtraForm(request.POST, instance=extra)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('extra_inventory')
    else:
        form = AddExtraForm(instance=extra)
    return render(request, 'edit_extra.html', {'form': form})

@login_required
def check_stock_recipe(request):
    recipes = Recipe.objects.filter(user=request.user)

    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('recipe_inventory')
    else:
        form = AddRecipeForm()

    context = {'recipes' : recipes, 'form': form}
    return render(request, 'recipe_inventory.html', context)



@login_required
def remove_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id, user=request.user)
    recipe.delete()
    return redirect('recipe_inventory')

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id, user=request.user)
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('recipe_inventory')
    else:
        form = AddRecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    user = request.user
    malts = recipe.Malts.all()
    boilings = recipe.Boilings.all()
    yeasts = recipe.Yeasts.all()
    fermentations = recipe.Fermentations.all()
    brewings = recipe.Brewings.all()
    
    context = {
        'recipe': recipe,
        'malts': malts,
        'boilings': boilings,
        'yeasts' : yeasts,
        'fermentations': fermentations,
        'brewings': brewings,
        
    }
    return render(request, 'recipe_detail.html', context)

def recipe_detail_read(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    user = request.user
    malts = recipe.Malts.all()
    boilings = recipe.Boilings.all()
    yeasts = recipe.Yeasts.all()
    fermentations = recipe.Fermentations.all()
    brewings = recipe.Brewings.all()
    Likes = recipe.Likes.all()
    is_liked = False 
    for like in Likes:
        if like.user == user:
            is_liked = True
            break  

    context = {
        'recipe': recipe,
        'malts': malts,
        'boilings': boilings,
        'yeasts' : yeasts,
        'fermentations': fermentations,
        'brewings': brewings,
        'is_liked': is_liked,
    }
    return render(request, 'recipe_detail_read.html', context)



@login_required
def select_malt(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    stock_malts = StockMalt.objects.filter(user=request.user)
    if request.method == 'POST':
        form = MaltForm(request.POST, user=request.user)
        if form.is_valid():
            stock_malt_id = int(form.cleaned_data['stock_malt'])  
            stock_malt = StockMalt.objects.get(id=stock_malt_id)  
            Malt.objects.create(
                recipe=recipe,
                stockMalt=stock_malt,
                quantity=form.cleaned_data['quantity']
            )
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = MaltForm(user=request.user)
    return render(request, 'select_malt.html', {'form': form, 'stock_malts': stock_malts})

@login_required
def remove_recipe_malt(request, malt_id, recipe_id):
    malt = get_object_or_404(Malt, pk=malt_id)
    malt.delete()
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def create_brewing(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = BrewingForm(request.POST)
        if form.is_valid():
            Brewing.objects.create(
                recipe=recipe,
                temperature = form.cleaned_data['temperature'],
                time = form.cleaned_data['time']
            )
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = BrewingForm()
    return render(request, 'create_brewing.html', {'form': form})

@login_required
def remove_recipe_brewing(request, brewing_id, recipe_id):
    brewing = get_object_or_404(Brewing, pk=brewing_id)
    brewing.delete()
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def create_boiling(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = BoilingForm(request.POST)
        if form.is_valid():
            Boiling.objects.create(
                recipe=recipe,
                cool = form.cleaned_data['DryHopping'],
                time = form.cleaned_data['time'],
            )
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = BoilingForm()
    return render(request, 'create_boiling.html', {'form': form})

  
@login_required
def remove_recipe_boiling(request, boiling_id, recipe_id):
    boiling = get_object_or_404(Boiling, pk=boiling_id)
    boiling.delete()
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def add_boiling_hop(request, boiling_id):
    boiling = Boiling.objects.get(id=boiling_id)
    stock_hops = StockHop.objects.filter(user=request.user)
    if request.method == 'POST':
        form = HopForm(request.POST, user=request.user)
        if form.is_valid():
            stock_hop_id = int(form.cleaned_data['stock_hop'])
            stock_hop = StockHop.objects.get(id=stock_hop_id)
            Hop.objects.create(
                boiling=boiling,
                stockHop=stock_hop,
                quantity=form.cleaned_data['quantity']
                )
            return redirect('recipe_detail', recipe_id=boiling.recipe.id)
    else:
        form = HopForm(user=request.user)
    return render(request, 'add_boiling_hop.html', {'form': form, 'stock_hops': stock_hops, 'boiling': boiling})

@login_required
def remove_boiling_hop(request, recipe_id, hop_id):
    hop = get_object_or_404(Hop, pk=hop_id)
    hop.delete()
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def add_boiling_extra(request, boiling_id):
    boiling = Boiling.objects.get(id=boiling_id)
    stock_extras = StockExtra.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ExtraForm(request.POST, user=request.user)
        if form.is_valid():
            stock_extra_id = int(form.cleaned_data['stock_extra'])
            stock_extra = StockExtra.objects.get(id=stock_extra_id)
            Extra.objects.create(
                boiling=boiling,
                stockExtra=stock_extra,
                quantity=form.cleaned_data['quantity']
                )
            return redirect('recipe_detail', recipe_id=boiling.recipe.id)
    else:
        form = ExtraForm(user=request.user)
    return render(request, 'add_boiling_extra.html', {'form': form, 'stock_extras': stock_extras, 'boiling': boiling})

@login_required
def remove_boiling_extra(request, recipe_id, extra_id):
    extra = get_object_or_404(Extra, pk=extra_id)
    extra.delete()
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def add_recipe_yeast(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    stock_yeasts = StockYeast.objects.filter(user=request.user)
    if request.method == 'POST':
        form = YeastForm(request.POST, user=request.user)
        if form.is_valid():
            stock_yeast_id = int(form.cleaned_data['stock_yeast'])
            stock_yeast = StockYeast.objects.get(id=stock_yeast_id)
            Yeast.objects.create(
                recipe=recipe,
                stockYeast=stock_yeast,
                quantity=form.cleaned_data['quantity']
                )
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = YeastForm(user=request.user)
    return render(request, 'add_recipe_yeast.html', {'form': form, 'stock_yeasts': stock_yeasts, 'recipe': recipe})

@login_required
def remove_recipe_yeast(request, recipe_id, yeast_id):
    yeast = get_object_or_404(Yeast, pk=yeast_id)
    yeast.delete()
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def create_fermentation(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == 'POST':
        form = FermentationForm(request.POST)
        if form.is_valid():
            Fermentation.objects.create(
                recipe=recipe,
                temperature = form.cleaned_data['temperature'],
                time = form.cleaned_data['time'],
            )
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = FermentationForm()
    return render(request, 'create_fermentation.html', {'form': form})

  
@login_required
def remove_recipe_fermentation(request, fermentation_id, recipe_id):
    fermentation = get_object_or_404(Fermentation, pk=fermentation_id)
    fermentation.delete()
    return redirect('recipe_detail', recipe_id=recipe_id)

def recipe_calculations(request, recipe_id):
    recipe = get_object_or_404(Recipe,pk=recipe_id)
    cost = 0 
    EBC = 0
    IBU = 0
    PPG = 37
    efficiency = 0.75
    Alcool = 0
    totmass = 0
    volume = recipe.volume
    for boiling in recipe.Boilings.all() :
        time = boiling.time
        for hop in boiling.Hops.all() :
            alpha = hop.stockHop.alpha
            mass= hop.quantity
            cost += hop.stockHop.cost * mass/100
            IBU += (1.65*(0.000125)**(1.06-1))*(1-exp(-0.04*time))*((alpha/100)*mass*1000)/(4.15*volume)
        for extra in boiling.Extras.all() :
            cost += extra.stockExtra.cost * extra.quantity
    for malt in recipe.Malts.all() :
        mass = malt.quantity
        cost += malt.stockMalt.cost * mass
        color = malt.stockMalt.ebc/2.65
        MCU = color*2.2046*mass/(volume*0.264)
        if MCU >= 25 :
            EBC += 1.4922*(MCU**0.6859)
        else :
            EBC += MCU
        totmass += mass*2.2046
    for yeast in recipe.Yeasts.all() :
        cost += yeast.quantity * yeast.stockYeast.cost

    EBC = 1.97*EBC
    GU = totmass * PPG * efficiency
    OG = 1+(GU/(volume*0.264))/1000
    FG = OG - (OG-1)*0.75
    alcool = (OG-FG)*131
    recipe.ebc = EBC
    recipe.ibu = IBU
    recipe.alcool = alcool
    recipe.cost = cost

    recipe.save()
    return redirect('recipe_detail',recipe_id = recipe_id)
    
@login_required
def advanced_edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id, user=request.user)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = EditRecipeForm(instance=recipe)
    return render(request, 'advanced_edit_recipe.html', {'form': form})

def recipe_stock(request,recipe_id):
    if request.method =="POST":
        recipe = get_object_or_404(Recipe, pk=recipe_id, user=request.user)
        if request.POST.get('confirmed') == 'true':
            for malt in recipe.Malts.all() :
                stockmalt = get_object_or_404(StockMalt, pk=malt.stockMalt.id)
                stockmalt.quantity -= malt.quantity
                stockmalt.save()
            for yeast in recipe.Yeasts.all() :
                stockyeast = get_object_or_404(StockYeast, pk=yeast.stockYeast.id)
                stockyeast.quantity -= yeast.quantity
                stockyeast.save()
            for boiling in recipe.Boilings.all() :
                for hop in boiling.Hops.all():
                    stockhop = get_object_or_404(StockHop, pk=hop.stockHop.id)
                    stockhop.quantity -= hop.quantity
                    stockhop.save()
                for extra in boiling.Extras.all() :
                    stockextra = get_object_or_404(StockExtra, pk=extra.stockHop.id)
                    stockextra.quantity -= extra.quantity
                    stockextra.save()
            return redirect('recipe_detail',recipe_id = recipe_id)
        else :
            return redirect( 'recipe_detail',recipe_id=recipe_id)
    
def recipe_stock_confirm(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id, user=request.user)
    context = {
        'recipe': recipe,
    }
    return render(request, 'recipe_stock_confirm.html', context)

@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    user = request.user
    try:
        like = Like.objects.get(user=user, recipe=recipe)
        like.delete()
    except Like.DoesNotExist:
        like = Like.objects.create(user=user, recipe=recipe)
    return redirect('recipe_detail_read', recipe_id=recipe_id)

def liked_recipes (request) :
    user = request.user
    likes = Like.objects.filter(user=user)
    recipes = [like.recipe for like in likes]

    context = {
        'user': user,
        'recipes': recipes,
    }
    return render(request, 'liked_recipes.html', context)


def recipe_search(request):
    search_query = request.GET.get('search_query', '')
    sort_by = request.GET.getlist('sort_by')
    descending = 'descending' in request.GET

    recipes = Recipe.objects.filter(Q(name__icontains=search_query) | Q(family__icontains=search_query))

    # Apply sorting
    if sort_by:
        ordering = []
        for field in sort_by:
            if descending:
                field = '-' + field
            ordering.append(field)
        recipes = recipes.order_by(*ordering)

    paginator = Paginator(recipes, 10)  # Display 10 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'recipes': recipes,
        'search_query': search_query,
        'sort_by': sort_by,
        'descending': descending,
    }
    return render(request, 'recipe_search.html', context)

def get_random_recipe(request):
    public_recipes = Recipe.objects.filter(private=False)
    recipe_count = public_recipes.count()
    
    if recipe_count > 0:
        random_index = random.randint(0, recipe_count - 1)
        random_recipe = public_recipes[random_index]
        recipe_id = random_recipe.id
        return recipe_detail_read(request, recipe_id)
    
    else :
        return render(request,'index.html')








    








