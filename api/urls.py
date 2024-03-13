from django.urls import path, include

from . import views

app_name = "api"
urlpatterns = [
    path("countries/", views.CountryView.as_view(), name="countries"),
    path("states/", views.StateView.as_view(), name="states"),
    path("countries/<str:country_code>/states/", views.CountryStateListView.as_view(), name="states_detail"),
]