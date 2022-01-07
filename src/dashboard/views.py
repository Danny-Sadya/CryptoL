from django.shortcuts import render
from .forms import *

# Create your views here.

def dashboard_view(request):
    """Main page rendering"""
    form = SearchForm
    return render(request, 'temp/index.html', context={'form': form})
