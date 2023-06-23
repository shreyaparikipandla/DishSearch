
# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from .models import Dish

def search_view(request):
    query = request.GET.get('q', '')
    results = Dish.objects.filter(name__icontains=query)
    context = {'query': query, 'results': results}
    return render(request, 'search.html', context)
