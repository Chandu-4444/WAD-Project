from django.shortcuts import redirect, render


# Create your views here.

def index(request):
    if request.method=="GET":
        print("Inside GET")
        return render(request, 'Index Page/index.html', {"form":UserCreation})
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'After Login/home.html')
            else:
                return HttpResponse('<h1>Wrong</h1>')
        else:
            return HttpResponse('<h1>Username cannot be empty</h1>')

