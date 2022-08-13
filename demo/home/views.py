from django.shortcuts import render

# Create your views here.

def get_home(request):
    # return render(request, 'home.html')
    return render(request, template_name = "home.html", context={"name":"Ngoc Anh"})