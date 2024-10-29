from django import forms

class CreateNewTask(forms.Form):
    #Enviar los datos al html, no a la base de datos. AL HTML!!
    title = forms.CharField(label="Title", max_length=200)
    description = forms.CharField(label="Task description",widget=forms.Textarea)
    done = forms.BooleanField(label="Done", required=False)