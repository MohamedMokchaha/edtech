from django.urls import path
from . import views
from .views import (
    FinanciementView,
    CandidateView,
    FormationListView,
    FormationDetailView,
    ChatGPTView,
    ExpositionView, DataView, BlockchainView, Skills,
)

app_name = "financiement"

urlpatterns = [
    path("", views.offer_list_view, name='offer_list'),
    path("candidate/", CandidateView.as_view(), name="candidate"),
    path('cours/', views.formations, name='formations'),
    path("formation/<int:pk>/", FormationDetailView.as_view(), name="formation_detail"),
    path("chatgpt/", ChatGPTView.as_view(), name="chatgpt"),
    path("exposition/", ExpositionView.as_view(), name="exposition"),
    path("data&IA/", DataView.as_view(), name="data&IA"),
    path("blockchain/", BlockchainView.as_view(), name="Blockchain"),
    path("skills/", Skills.as_view(), name="skills"),
]
