from django.urls import path, include
from django.contrib import admin
from monapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    # path('', include('monapp.urls')), # Inclure les routes de "monapp"
    path('admin/', admin.site.urls),
    path('about_me/', views.about_me, name='about_me'),
    path('interests/', views.interests, name='interests'),
    path('skills/', views.skills, name='skills'),
    
    path('chatbot/', views.chatbot, name='chatbot'),
    path('competitions/', views.competitions, name='competitions'),  # Lien vers la vue `competitions`
    path('contacts/', views.contacts, name='contacts'),
    path('projects/', views.mes_projects, name='mes_projects'),
    path('projects/fraud_detection/', views.project_fraud_detection, name='project_fraud_detection'),
    path('projects/turbulence/', views.project_turbulence, name='project_turbulence'),
    path('projects/ghana/', views.project_ghana, name='project_ghana'),
    path('projects/ab_testing/', views.project_ab_testing, name='project_ab_testing'),
    path('projects/regression/', views.project_regression, name='project_regression'),
    path('projects/time_series/', views.project_time_series, name='project_time_series'),
    path('projects/deep_learning/', views.project_deep_learning, name='project_deep_learning'),
    path('projects/generative_ai/', views.project_generative_ai, name='project_generative_ai'),
    path('projects/gpt_llama/', views.project_gpt_llama, name='project_gpt_llama'),
    path('projects/recommendation_systems/', views.project_recommendation_systems, name='project_recommendation_systems'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

