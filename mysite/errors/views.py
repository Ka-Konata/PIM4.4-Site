from django.shortcuts import render

# Create your views here.
def error403(request):
    context = {}
    return render(request, "erros/403.html", context)