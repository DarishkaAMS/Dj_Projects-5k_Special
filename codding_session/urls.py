from django.urls import path

from codding_session import views

urlpatterns = [
    path('', views.codding_session_page_view, name="codding_session_page_view"),
    path('home/', views.codding_session_page_view, name="codding_session_page_view")
]