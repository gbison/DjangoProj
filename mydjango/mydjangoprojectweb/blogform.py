from django import forms
from mydjangoprojectweb.models import Blog   # Importing the forms Module of Django 

class BlogForm(forms.ModelForm):    # Define a Modelform which will interact with our Database on backend. Inherits From base class in models.py file under myproject/blogapp directory
      title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':'title','class':'input-field form-control', 'placeholder': "Blog Title", }))
      email = forms.EmailField(widget=forms.TextInput(attrs={'id':'email','class':'input-field form-control', 'placeholder': "Your Email Address"}))
      content = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'id':'content','class':'textarea form-control', 'rows':'4'}))

      class Meta:           # This is mandatory to create form using model form, telling Django the details of how we want it done ie., Which fields from above mentioned blog Model should be used when creating a new entry for this Form – which are all.  
        model = Blog        # The Database Model that will interact with our database via this form - Here its 'Blog' defined in models.py file under myproject/blogapp directory
        fields = ['title','email','content']    # Fields of the above mentioned blog post creation which need to be filled by users while creating a new entry for Blog Post – here, title & content field are required..  