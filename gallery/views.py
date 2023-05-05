from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from .form import ImageForm
from .models import ImageModel
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from .serializers import GallerySerializer

# Create your views here.
class GalleryViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = ImageModel.objects.all()
    # The serializer class for serializing output
    serializer_class = GallerySerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]

@csrf_exempt
def gallery(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_img = form.save()
            # Get the current instance object to display in the template
            # img_obj = form.instance
            # return JsonResponse({"img_id": new_img.id})
            response = HttpResponse()
            # response.headers["img_id"] = new_img.id+'|' + new_img.img
            response.headers["img_id"] = new_img.img

            return response
    else:
        form = ImageForm()
    return render(request, "template/gallery.html", {"form": form})

class ExceptionLoggingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.body)
        print(request.scheme)
        print(request.method)
        print(request.META)

        response = self.get_response(request)

        return response
    
class showImg(DetailView):
    model = ImageModel
    template_name = 'showImg.html'
    context_object_name = 'GallImg'

class showPic(DetailView):
    model = ImageModel
    template_name = 'pics.html'
    context_object_name = 'GallPic'
