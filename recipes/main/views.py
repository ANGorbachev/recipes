from django.shortcuts import render, redirect
from .models import Recipes
from .forms import RecipesForm
from django.views.generic import DetailView, UpdateView, DeleteView

class RecipesDetailView(DetailView):
    model = Recipes
    template_name = "main/detail_view.html"
    context_object_name = "recipe"

class RecipesUpdateView(UpdateView):
    model = Recipes
    template_name = "main/add.html"
    form_class = RecipesForm

class RecipesDeleteView(DeleteView):
    model = Recipes
    template_name = "main/confirm_delete.html"
    success_url = "/"


def index(request):
    tag_query = request.GET.get('tags', '')
    search_query = request.GET.get('search', '')
    meal_list = Recipes.objects.filter(title__iregex=search_query, tags__iregex=tag_query)
    data = {
        "meal_list": meal_list,
    }
    return render(request, "main/index.html", data)


def about(request):
    return render(request, "main/about.html")\

def add(request):
    error = ''
    if request.method == "POST":
        form = RecipesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            print(form)
            print(form.errors)
            error = 'Форма заполнена некорректно'
    form = RecipesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, "main/add.html", data)
