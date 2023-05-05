from django.urls import path

from .views import gallery, showImg, showPic

urlpatterns = [
    path("", gallery, name="gallery"),
    path("image/<int:pk>", showPic.as_view(), name="pics" ),
    path("longimage/<int:pk>", showImg.as_view(), name="showImg" )
]