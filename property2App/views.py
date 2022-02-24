from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "propertyName": "La Propriedad",
        "propertyLocation": "H-Town, Tx",
        "propertyHomies": ["Su Casa", "Mi Casa", "Casa Blanca", "Nuevo Camino"]
    }
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("All about our Project application!")


def contributors(request):
    return HttpResponse("This will show who contributed to the project and application")

def test(request):
    return render(request, "test.html")

def form(request):
    # return render(request, "propertyForm.html" )
    if request.method == "GET":
        print("GET request was made for propertyForm.html")
        return render(request, "propertyForm.html")
    if request.method == "POST": 
        print("POST request was made for propertyForm.html")

def form(request):
    # return render(request, "propertyForm.html")
    if request.method == "GET":
        print("GET request was made for propertyForm.html")
        return render(request, "propertyForm.html")
    if request.method == "POST":
        print("Post request was made for propertyForm.html")