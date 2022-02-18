# IMPORTS 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Third party
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, reverse, redirect

# Internal
from .models import Brand
from .forms import BrandForm

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def show_brand(request):
    """
    View to return all brands ordered alphabetically
    Args:
        request (object): HTTP request object
    Returns:
        Brand page with passed context object
    """
    # Credit for sort Brand.objects method: Reddit
    brands = Brand.objects.all().order_by('name')    
    context = {
        'brands': brands,
    }

    return render(request, 'brands/brands.html', context)

@login_required
def add_brand(request):
    """
    View to add brands 
    Args:
        request (object): HTTP request object
    Returns:
        Add brand page with context
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            brand = form.save()
            messages.success(request, 'Successfully added brand!')
            return redirect(reverse('brands'))
        else:
            messages.error(request, 'Failed to add brand. Please ensure the form is valid.')
    else:
        form = BrandForm()

    template = 'brands/add_brand.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_brand(request, brand_name):
    """
    View to edit pre-existing brands 
    Args:
        request (object): HTTP request object
    Returns:
        Edit brand page with context
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    brand = get_object_or_404(Brand, name=brand_name)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated brand!')
            return redirect(reverse('brands'))
        else:
            messages.error(request, 'Failed to update brand. Please ensure the form is valid.')
    else:
        form = BrandForm(instance=brand)
        messages.info(request, f'You are editing {brand.name}')

    template = 'brands/edit_brand.html'
    context = {
        'form': form,
        'brand': brand,
    }

    return render(request, template, context)


@login_required
def delete_brand(request, brand_name):
    """
    View to delete pre-existing brands 
    Args:
        request (object): HTTP request object
    Returns:
        Generic brands page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    brand = get_object_or_404(Brand, name=brand_name)
    brand.delete()
    messages.success(request, 'Brand deleted.')
    return redirect(reverse('brands'))
