from django import forms
from .models import Category, Post

class SearchForm(forms.Form):
    query = forms.CharField(max_length=20)
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # exclude = ('author', )
        widgets = {
            'author': forms.HiddenInput(),
            'content': forms.Textarea(attrs={'rows': 3,
                                             'class': 'content_class'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' in title:
            raise forms.ValidationError('Cannot include Django in the title')
        else:
            return title
        
    def clean(self):
        clean_data = super().clean()
        title = clean_data['title']
        content = clean_data['content']
        author = clean_data['author']

        if author.user.username == 'jd' and 'Django' in content:
            raise forms.ValidationError('Cannot include Django in the content')
        else:
            return clean_data
        

CategoryFormSet = forms.modelformset_factory(Category, form=CategoryForm, extra=0)

PostFormSet = forms.modelformset_factory(Post, form=PostForm, extra=0)


# CategoryRelatedFormSet = forms.inlineformset_factory(Post, Category, form=CategoryForm, extra=0)
# PostFormSet = forms.inlineformset_factory(Category, Post, form=PostForm, extra=0)