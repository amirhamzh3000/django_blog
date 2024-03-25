from django import forms
from .models import Todo

class TOdoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()


class TOdoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title','body','created')