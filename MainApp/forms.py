from django.forms import ModelForm
from MainApp.models import Snippet
from django.forms import TextInput, Textarea


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code', 'rate']

        labels = {
            "name": ""
        }

        widgets = {
            "name": TextInput(attrs={"placeholder": "Название виджета","class": "name"})
        }
