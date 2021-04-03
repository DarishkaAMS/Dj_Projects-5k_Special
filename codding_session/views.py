from django.shortcuts import render, HttpResponse

# Create your views here.


def codding_session_page_view(request):
    return render(request, template_name='codding_session/all.html')
