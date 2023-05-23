from inspect import formatannotationrelativeto
from django.shortcuts import render, HttpResponse, redirect
import random
from .models import Neighbor

# Create your views here.

TICKETS = {
    "souvenirs": (4,9),
    "food": (2,7),
    "tShirts": (10,20),
    "stuffedAnimals": (5,15),
}

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

def skills(request):
    return render(request, "skills.html")

# Without Sessions and Redirect

# def form(request):
#     return render(request, "propertyForm.html")
#     # if request.method == "GET":
#     #     print("GET request was made for propertyForm.html")
#     #     return render(request, "propertyForm.html")
#     # if request.method == "POST":
#     #     print("Post request was made for propertyForm.html")

# def results(request):
#     if request.method == "POST":
#         context = {
#             'memberName': request.POST['memberName'],
#         }
#         return render(request, 'results.html', context)
#     return render(request, 'results.html')

def form(request):
    return render(request, 'propertyForm.html')

def newMembers(request):
    if request.method == 'GET':
        return redirect('/form/')
    request.session['results'] = {
        'memberName': request.POST['memberName'],
    }
    return redirect('/results')

def results(request):
    context = {
        'results': request.session['results'],
    }
    return render(request, 'results.html', context)

def theShop(request):
    if not "price" in request.session:
        request.session['price'] = 0
    return render(request, 'thePropertyShop.html')

def reset(request):
    request.session.clear()
    return redirect('/the-shop')

def purchase(request):
    if request.method == 'GET':
        return redirect('/the-shop/')

    itemName = request.POST['categories']
    categories = TICKETS[itemName]

    currTotal = random.randint(categories[0], categories[1])

    result = 'total'

    request.session['price'] += currTotal
    return redirect('/the-shop')

#Display our newly added Neighbor
def neighbor(request):
    context = {
        "allNeighbor": Neighbor.objects.all().values()
    }
    return render(request, 'neighbor.html', context)

def addNeighbor(request):
    return render(request, 'newNeighbor.html')

def create(request):
    if request.method == 'GET':
        return redirect('/addNeighbor/')
    Neighbor.objects.create(
        neighborName=request.POST['neighborName'],
        neighborType=request.POST['neighborType'],
        neighborBirthDay=request.POST['neighborBirthDay']
    )

    return redirect('/neighbor/') 