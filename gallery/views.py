from django.shortcuts import render
from .models import Image,Category,Location

# Create your views here.
def index(request):
    images = Image.get_all_images()
    return render(request, 'index.html', {'images':images})

def search_image(request):
    name = 'Search'
    categories = Category.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html', {'name':name, 'images':found_results, 'message':message, 'categories':categories})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html',{'message':message})

def location_filter(request, id):
    locations = Location.objects.all()
    location = Location.get_location_id(id=id)
    images = Image.filter_by_location(image_location)
    name = f'{location} Photos' 
    return render(request, 'location.html', {'name':name, 'images':images, 'locations':locations, 'location':location})

def detail(request, pk):
    image = Image.objects.get(pk=pk)
    context = {
        'image': image
    }
    return render(request, 'detail.html', context)