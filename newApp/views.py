from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home.html',{})

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			message.success(request, "Account created successfully!")