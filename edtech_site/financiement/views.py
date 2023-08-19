from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import CandidateForm
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (Offer,Candidate)
from  edtech_app.models import (cours,)
# Create your views here.

class FinanciementView(LoginRequiredMixin,TemplateView):
    
    template_name = './financement/financement.html'
    login_url = '/signup/'
    
    def get_context_data(self, **kwargs):
        salarie_list = []
        context = super().get_context_data(**kwargs)
        context['demander'] = Offer.objects.filter(type="demandeur")
        context['salarie'] = Offer.objects.filter(type="salarie")
        context['travailleur'] = Offer.objects.filter(type="travailleur")
        context['alternance'] = Offer.objects.filter(type="alternance")

        return context 

class CandidateView(LoginRequiredMixin,FormView):
    
    #only the authenticated user can access this view
    
    form_class = CandidateForm
    template_name = './financement/candidate.html'
    fields = ['name','last_name','study_level','section','diploma']
    success_url = '/financement'
    login_url = '/signup/'

    
    # verify form validity
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if (form.is_valid()):
            '''
            Check if the candidate has already applied for this offer
            '''
            if Candidate.objects.filter(name = form.cleaned_data['name']).exists():
                messages.error(self.request,"Vous avez deja postuler pour cette offre")
            form.save()
        return super().form_valid(form)
        

class FormationListView(LoginRequiredMixin,ListView):
    template_name = './financement/formation.html'
    queryset = cours.objects.all()  
    context_object_name = 'courses'
    login_url = '/signup/'

        

class FormationDetailView(LoginRequiredMixin,DetailView):
    template_name = './financement/formation_detail.html'
    login_url = '/signup/'
    model = cours
    context_object_name = 'course'

class ChatGPTView(LoginRequiredMixin, TemplateView):
    template_name = 'financement/formation/chatgpt.html'
    login_url = '/signup/'

class ExpositionView(LoginRequiredMixin, TemplateView):
    template_name = 'financement/formation/exposition.html'
    login_url = '/signup/'

class DataView(LoginRequiredMixin, TemplateView):
    template_name = 'financement/formation/data.html'
    login_url = '/signup/'


class BlockchainView(LoginRequiredMixin, TemplateView):
        template_name = 'financement/formation/blockchain.html'
        login_url = '/signup/'

class Skills(LoginRequiredMixin, TemplateView):
            template_name = 'financement/formation/skills.html'
            login_url = '/signup/'

def formations(request):
    cours_list = cours.objects.all()  # Récupère tous les cours depuis la base de données
    context = {'cours_list': cours_list}  # Crée un contexte avec la liste des cours
    return render(request, 'financement/formation.html', context)



def offer_list_view(request):
    offers = Offer.objects.all()
    context = {'offers': offers}
    return render(request, 'financement/financement.html', context)


   
        
