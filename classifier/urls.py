from django.urls import path
from classifier.views import index

app_name = "classifier"

urlpatterns = [
    path("", index, name="index"),
]