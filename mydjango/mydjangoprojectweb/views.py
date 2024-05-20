#import the needed library for using the render function
from django.shortcuts import get_object_or_404, redirect, render
from mydjangoprojectweb.blogform import BlogForm
from mydjangoprojectweb.models import Blog

#function calls to render an html page.
def homepage (requests):
    return render(requests, 'home.html')

def aboutpage (requests):
    return render(requests, 'about.html')

def contactpage (requests) :
    return render(requests, 'contact.html')

def create_blog(request):                   # View function to handle incoming HTTP requests and return appropriate responses - here we are handling the creation of blog posts via this view   
    if request.method == "POST":          # If user has submitted some data through form (i.e., POST method) then perform following operations  
        form = BlogForm(request.POST)    # Create a Form instance with posted Data from HTTP Request, in other words bind Posted Data to the Django's Modelform i.e., 'BlogForm'. This is how you can get data back into your forms after POST request – which will allow users to fill it out again if they encounter errors on submission
        if form.is_valid():               # If all fields in Form are valid  
            newblog = Blog(title=form.cleaned_data['title'], email=form.cleaned_data['email'], content=form.cleaned_data['content'])  # Create a New blog object but do not save it to the database - here, clean data means that we have checked & cleaned up/normalized our form's input ie., 'Title', and 'Content'. This is how you can access validated user inputs after POST request
            newblog.save()               # Save this New blog object into SQLite Database – Here, saving to database ensures changes are permanent  
    else:
        form = BlogForm()                # Create an empty, unbound form
    return render(request,'create_blog.html',{'form':form})   # Return a rendered Response to HTTP Request with our Form which will be displayed on webpage as per 'create_blog.html' template that we have defined in templates directory of myproject/myapp application – here, This is how you can pass form data into your HTML Templates for user interactio  

# In your views, import the models where you have defined them ie., from .models import Blog. This allows us access/functionality of blogs model like creating new blog post etc.. – this way we can interact with database directly through Django ORM & handle all kinds of operations. For example fetching existing data or updating it
def show_blogs(request):      # View function to display Blog posts on our site using these retrieved data
     blogs = Blog.objects.all()    # This is how you can get all objects from your model ie., Database Table – this way we are fetching every single blog post that currently exists in database etc.. For example creating new field with name 'title' as per defined Comment Model and then getting its value using title = form['name'].value()
     return render(request, "show_blog.html", {"allBlogs": blogs})    # Return a rendered Response to HTTP Request – this way we are passing all retrieved data/objects ie., blog posts etc.. from our database directly into 'showAllPosts' HTML Template which is inside templates directory of myproject application where it can be displayed on webpage
 
def edit_blog(request, id):
    #https://stackoverflow.com/questions/4673985/how-to-update-an-object-from-edit-form-in-django
    try:
        blog = get_object_or_404(Blog, id=id)
    except Blog.DoesNotExist:
        print("THe BLOG you are referenceing does not exist, please check the ID to ensure it matches with one in the database!")
    except Exception as e:
        raise e
        
    if request.method =='GET':
        return render (request, "edit_blog.html", {"form":BlogForm(instance=blog)})
    else:
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('showblog')
        else:
            return render(request,"edit_blog.html", {"form":form})
        
def read_blog(request, id):
    try:
        blog = get_object_or_404(Blog, id=id)
    except Blog.DoesNotExist:
        print("THe BLOG you are referenceing does not exist, please check the ID to ensure it matches with one in the database!")
    except Exception as e:
        raise e
    
    if request.method =='GET':
        return render (request, "readblog.html", {"form":BlogForm(instance=blog)})
    else:
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('showblog')
        else:
            return render(request,"readblog.html", {"form":form})
        
def delete_blog(request, id):
    try:
        blog = get_object_or_404(Blog, id=id)
        instance = Blog.objects.get(id=id)
        if instance is None or blog is None:
            pass
        else:
            return render (request, "show_blog.html", {'result':instance.delete(),'id':id})
    except Blog.DoesNotExist:
        print("THe BLOG you are referenceing does not exist, please check the ID to ensure it matches with one in the database!")
    except Exception as e:
        raise e

    
    