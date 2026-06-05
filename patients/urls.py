from django.urls import path
from .views import PatientAPIView

urlpatterns = [
    path('patients/', PatientAPIView.as_view()),
    path('patients/<int:id>/',PatientAPIView.as_view()
    ),
]