from django.shortcuts import render
from .models import Image
from .forms import ImageForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # show a success message or redirect
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def display_image(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'display.html', {'image': image})
