from django.shortcuts import  render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login
from .forms import NewUserForm, EditUserForm, CategoryForm, TaskForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Category, Task

#USER PROFILE MANAGEMENT
def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")

		messages.error(request, "Unsuccessful registration. Invalid information.")
		
	form = NewUserForm()
	return render(request, "registration/register.html", context={"form":form})

def showUserProfile(request):
	if request.method == "GET":
		current_user = request.user
		form_user = EditUserForm(instance=current_user)
		form_password = PasswordChangeForm(current_user)
		context={"form_user": form_user, "form_password": form_password}

		return render(request, "registration/update.html", context)

def editUserProfile(request):
	if request.method == "POST":
		form = EditUserForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			messages.success(request, "Update successful.")
		
		else:
			messages.error(request, "Update failed.")

	return redirect('showUserProfile')

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('showUserProfile')

        else:
            messages.error(request, 'Please correct the error below.')

    return redirect('showUserProfile')

#CATEGORY & TASK MANAGEMENT
def showCategoryTask(request):
	if request.method == 'GET':
		if request.user.is_authenticated:
			current_user = request.user
			categories = Category.objects.filter(user=current_user)
			tasks = Task.objects.filter(category__in=categories)
			form_cate = CategoryForm()
			form_task = TaskForm(user=current_user)
			context={"categories": categories, "tasks": tasks, "form_cate": form_cate, "form_task": form_task}
		
		else:
			context={"categories": None, "tasks": None, "form_cate": None, "form_task": None}
		
		return render(request, "home.html", context)

def addCategory(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save(commit=False)
			category.user = request.user
			category.save()
			messages.success(request, 'Category created!')
		
		else:
			messages.error(request, 'Error occurred!')
		
	return redirect('home')

def delCategory(request, id):
	if request.method == 'POST':
		category = Category.objects.get(pk=id)
		category.delete()
	
	return redirect('home')

def addTask(request):
	if request.method == 'POST':
		form = TaskForm(request.POST, user=request.user)
		print(form)
		if form.is_valid():
			form.save()
			messages.success(request, 'Task created!')
		
		else:
			messages.error(request, 'Error occurred!')
		
	return redirect('home')

def delTask(request, id):
	if request.method == 'POST':
		task = Task.objects.get(pk=id)
		task.delete()
	
	return redirect('home')