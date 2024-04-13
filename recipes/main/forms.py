from .models import Recipes
from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileField, FileInput

class RecipesForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'description', 'ingredients', 'instructions', 'cook_time', 'tags', 'photo']

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название блюда",
                'maxlength': 100,
                'required': True,
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Краткое описание блюда",
                'maxlength': 250,
                'required': True,
            }),
            "ingredients": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Список ингредиентов",
                'required': True,
            }),
            "instructions": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Инструкция по приготовлению",
                'required': True,
            }),
            "cook_time": NumberInput(attrs={
                'minlength': 1,
                'maxlength': 4,
                'required': True,
                'type': 'number'}),

            "tags": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Тэги блюда",
                'maxlength': 50,
                'required': True,
            }),
            "photo": FileInput(attrs={
                "class": "form-control",
                "placeholder": "Фото блюда",
                'required': True,
            }),
        }
