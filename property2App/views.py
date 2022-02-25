from django.shortcuts import render, HttpResponse, redirect

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

def form (request):
    if request.method == 'GET':
        return render(request, 'propertyForm.html')
    request.session['memberName'] = {
        'memberName': request.POST['memberName'],
    }
    return redirect('/results/')

def results(request):
    context = {
        'memberName': request.session['memberName'],
    }
    return render(request, 'results.html', context)