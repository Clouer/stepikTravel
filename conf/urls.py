from django.urls import path
from tours.views import MainView, DepartureView, TourView

urlpatterns = [
    path('', MainView.as_view()),
    path('departure/<str:departure>/', DepartureView.as_view()),
    path('tour/<int:tour_id>/', TourView.as_view()),
]
