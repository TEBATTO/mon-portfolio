from django.shortcuts import render
from .models import Project

# Vues principales
def home(request):
    return render(request, 'accueil.html')

# Vue pour "Courses" (ou remplacez par votre fonctionnalité actuelle)
def courses(request):
    return render(request, 'interests.html')  # Assurez-vous que le fichier HTML existe

from django.shortcuts import render

# Vue pour le Chatbot
def chatbot(request):
    return render(request, 'chatbot.html')  # Assurez-vous que le fichier 'chatbot.html' existe dans le dossier templates

def about_me(request):
    return render(request, 'about_me.html')  # À propos de moi

# Vue pour "Compétences"
def competitions(request):
    return render(request, 'skills.html')


def interests(request):
    return render(request, 'interests.html')  # Mes centres d'intérêts

def skills(request):
    return render(request, 'skills.html')  # Compétences

def contacts(request):
    return render(request, 'contacts.html')

# Vue pour afficher tous les projets
def mes_projects(request):
    projects = Project.objects.all()  # Récupère les projets depuis la base de données
    return render(request, 'projects/mes_projects.html', {'projects': projects})

# Vues pour les projets individuels
def project_fraud_detection(request):
    return render(request, 'projects/detection_de_fraude.html')

def project_turbulence(request):
    return render(request, 'projects/turbulence.html')

def project_ghana(request):
    return render(request, 'projects/menage_ghana.html')

def project_ab_testing(request):
    return render(request, 'projects/ab_testing.html')

def project_regression(request):
    return render(request, 'projects/regression.html')

def project_time_series(request):
    return render(request, 'projects/analyse_des_series_temporelles.html')

def project_deep_learning(request):
    return render(request, 'projects/deep_learning_classification.html')

def project_generative_ai(request):
    return render(request, 'projects/ia_generative.html')

def project_gpt_llama(request):
    return render(request, 'projects/utilisation_api_gpt_llama.html')

def project_recommendation_systems(request):
    return render(request, 'projects/systemes_de_recommandation.html')
