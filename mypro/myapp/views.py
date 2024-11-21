from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo_entry
from django.urls import reverse
from django.template import loader
# Display all todos
def todo(request):
    todos = Todo_entry.objects.all()
    template = loader.get_template('todo.html')# Retrieve all todo entries
    context = {
        'todos': todos,
    }
    return HttpResponse(template.render(context, request))
# Add new todo entry
def add(request):
    if request.method == 'POST':
        entry = request.POST.get('entry')  
        if entry:
            Todo_entry.objects.create(title=entry)  
        return HttpResponseRedirect(reverse('todo'))  
    return HttpResponse(status=405)

# Delete a specific todo entry by id
def delete(request, id=None):
    if id:
        Todo_entry.objects.filter(id=id).delete()
    else:
        return HttpResponse("ID parameter missing", status=400)
    return HttpResponseRedirect(reverse('todo'))

# Delete all todo entries
def delete_all(request):
    if request.method == 'POST':
        Todo_entry.objects.all().delete()  # Delete all todo entries
        return HttpResponseRedirect(reverse('todo'))  # Redirect to the todo list
    return HttpResponse(status=405)  # Method Not Allowed if not POST
