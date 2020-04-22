from django.shortcuts import render

# Create your views here.
def front_page_view(request):
    return render(request, 'appy2/front_page.html')