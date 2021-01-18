from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html" )

def processGiftSubmission(request):
    print("we just submitted the form and are in the processGiftSubmission function")
    # print(request.method)
    print(request.POST) #request.POST represents the information collected from the from
    # <QueryDict: {'csrfmiddlewaretoken': ['26prbos5A9VaFvao0VfJToGPcvQ7Q4liqNg2Sl0DDs956oT2PQxlUbkAldPlNdZa'], 'reciepient': ['Zavian'], 'giver': ['Rob'], 'shoeChoice': [''], 'message': ['Getting the diggity darn buckets out here!']}>

    context = {
        'formInfo': request.POST
    }
    return render(request, "result.html", context)