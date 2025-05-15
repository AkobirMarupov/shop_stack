from django.shortcuts import render, get_list_or_404, redirect

from .models import Category
from .forms import CategoryForm


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})


def category_detail(request, pk):
    category = get_list_or_404(Category, pk=pk)
    return render(request, 'products/category_list.html', {'categories': category})


def category_create(request):
    if request.method == 'POST':
        form =CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    
    else:
        form = CategoryForm()
    return render(request, 'products/category_form.html', {'form': form})



