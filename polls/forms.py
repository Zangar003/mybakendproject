from django import forms
from .models import *
#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label = 'title')
    slug = forms.SlugField(max_length=255, label = 'URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}), label='Content')
    is_published = forms.BooleanField(label ='publication', required=False, initial=True)
    # picture = forms.ImageField(label = "image")
    email = forms.EmailField(label="email")
    questiopn_text = forms.CharField(max_length=200, label ="question")
    pub_date = forms.DateTimeField(label ="data")
    class Meta:
        model = Form_lab
        fields ="__all__"

class EmailForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='message')