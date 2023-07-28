from django.shortcuts import render
from .forms import TodoForm, CategoryForm, DoneForm
from .models import Todo, Category
from datetime import date


def add_todo_view(request):
# POST
    if request.method == 'POST':
        form_filled = TodoForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
        else:
            print(form_filled.errors)
            
# GET
    todo_form = TodoForm()
    context = {'form': todo_form}
    return render(request, 'add_todo.html', context)


def add_category_view(request):
# POST
    if request.method == 'POST':
        form_filled = CategoryForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
        else:
            print(form_filled.errors)
            
# GET
    category_form = CategoryForm()
    context = {'form': category_form}
    return render(request, 'add_category.html', context)


# display_todos : where all the todos are displayed. For each todo, you need to display:
# the title, the details,
# the date_creation, the deadline_date,
# the category of the todo,

def display_todos(request):

    # POST
    if request.method == 'POST':
       print(request.POST)
       todo = Todo.objects.get(id=request.POST['instance'])
       print(todo)
       todo.has_been_done = True
       todo.date_completion = date.today()
       todo.save()

    # GET
    todo_list = Todo.objects.all()
    todo_forms = []
    for todo in todo_list:
        form = DoneForm(initial={'instance': todo})
        todo_forms.append((todo, form))
    
    context = {'todos_forms': todo_forms}
    return render(request, 'todos.html', context)