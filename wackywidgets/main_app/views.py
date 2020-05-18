from django.shortcuts import render
from .models import Item
from django.views.generic.edit import CreateView, DeleteView

# Define the index view
def index(request):
  items = Item.objects.all()
  print(items)
  quantity = Item.objects.all()
  print(quantity)
  return render(request, 'index.html', {
    'items': items,
    'quantity': quantity,
  })

class ItemCreate(CreateView):
  model = Item
  fields = '__all__' 
  success_url = '/' 

class ItemDelete(DeleteView):
  model = Item
  success_url = '/' 