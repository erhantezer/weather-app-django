from django.urls import path

from weather.views import delete_city, index

urlpatterns = [
    path("", index, name="home"),
    path("delete/<int:id>", delete_city, name="delete" ),
]
