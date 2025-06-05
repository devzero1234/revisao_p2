from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.shortcuts import render, get_object_or_404, redirect

class TodoListView(ListView):
 model = Todo

class TodoCreateView(CreateView):
 model = Todo
 fields = ['title','deadline']
 success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
 model = Todo
 fields = ['title', 'deadline']
 success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
 model = Todo
 success_url = reverse_lazy('todo_list')

def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')

def todo_list(request):
    status = request.GET.get('status')
    order = request.GET.get('order')

    todos = Todo.objects.all()

    if status == 'completed':
        todos = todos.filter(completed=True)
    elif status == 'active':
        todos = todos.filter(completed=False)

    if order in ['due_date', 'priority']:
        todos = todos.order_by(order)

    return render(request, 'todos/todo_list.html', {'todos': todos})
