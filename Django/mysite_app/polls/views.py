from typing import Any, Dict
from django.shortcuts import render
from .models import Post, Person, Email, Category
from .forms import CategoryForm, PostForm, SearchForm, CategoryFormSet, PostFormSet
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, View
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

# 1. create superuser - add in the admin page a Person with first_name = 'ben'
# 2. create a AddPostView (CreateView) 


# class ManageCategories(View):

#     def get(self, request):
#         formset = CategoryFormSet(queryset=Category.objects.all())
#         context = {'formset': formset}
#         return render(request, 'manage_categories.html', context)
    
#     def post(self, request):
#         formset = CategoryFormSet(request.POST, queryset=Category.objects.all())
#         if formset.is_valid():
#             formset.save()
#         context = {'formset': formset}
#         return render(request, 'manage_categories.html', context)



def manage_categories(request):
    # POST
    if request.method == 'POST':
        formset = CategoryFormSet(request.POST, queryset=Category.objects.all())
        if formset.is_valid():
            formset.save()
    # GET
    formset = CategoryFormSet(queryset=Category.objects.all())
    context = {'formset': formset}
    return render(request, 'manage_categories.html', context)

def manage_posts(request):
    # POST
    if request.method == 'POST':
        formset = PostFormSet(request.POST, queryset=Post.objects.all())
        if formset.is_valid():
            formset.save()
    # GET
    formset = PostFormSet(queryset=Post.objects.all())
    context = {'formset': formset}
    return render(request, 'manage_posts.html', context)


current_user = Person.objects.get(first_name='Ivan')

@login_required(redirect_field_name=reverse_lazy('posts'), login_url=reverse_lazy('login'))
def add_post_view(request):

    if request.method == 'POST':
        data = request.POST
        filled_form = PostForm(data)
        filled_form.save()

    # GET
    post_form = PostForm(initial={'title': 'post !!!',
                                  'content': 'whatever',
                                  'author': current_user})
    
    context = {'form': post_form}
    return render(request, 'add_post.html', context)


# the class based alternative to add_post_view
class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add-post')
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('posts')

    def get_initial(self): # sets the 'initial' values for the form of the view
        user = self.request.user # the current user
        user_profile = user.user_profile # the current user's profile
        print('USER PROFILE', user_profile)
        return {'title': 'post !!!',
                'content': 'whatever',
                'author': user_profile}


# function based view
def add_category_view(request):
    
    if request.method == 'POST':
        data = request.POST
        filled_form = CategoryForm(data)
        filled_form.save()

    # GET
    category_form = CategoryForm()
    context = {'form': category_form}
    return render(request, 'add_category.html', context)


# class based view / generic view
class AddCategoryView(UserPassesTestMixin, CreateView):

    def test_func(self):
        if self.request.user.is_authenticated:
            return True
        else:
            return False

    model = Category
    # fields = ['name']
    form_class = CategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('add-category')

    def form_valid(self, form): # form_valid gives us control over how the form will be submitted 
        name = form.cleaned_data.get('name') # cleaned_data takes the data from the form and transforms to 
                                            # python native data type
        if name == 'Fantasy':
            form.instance.name = 'FANTASY 1000' # form.instance is the instance we are saving/updating
        return super().form_valid(form) # super() is a refernce to the parent class (CreateView)


def posts(request): 

    query = request.GET.get('query', None)
    if query:
        posts_all = Post.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        posts_all = Post.objects.all()
        
    search_form = SearchForm()
    context = {'post_list': posts_all, 'search': search_form}

    return render(request, 'posts.html', context)

# class based alternative to 'posts' view
class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'post_list'

    def get_queryset(self): # modifying / filtering the object list queryset

        query = self.request.GET.get('query', None) 
        if query:
            posts_all = Post.objects.filter(Q(title__icontains=query) | Q(author__first_name__icontains=query))
        else:
            posts_all = Post.objects.all()

        return posts_all # return what will be used as the post_list
    
    def get_context_data(self, **kwargs: Any): # for modifying the context dictionary 

        context = super().get_context_data(**kwargs) # getting the current context
        search_form = SearchForm()
        context['search'] = search_form # update the context

        return context 


# In the templates, display the email of the current user

def profile(request):

    user_addresses = current_user.addresses.all()
    user_email = current_user.email

    context = {'user': current_user, 'email': user_email, 'addresses': user_addresses}

    return render(request, 'profile.html', context)

