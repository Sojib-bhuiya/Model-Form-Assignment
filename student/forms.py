from django import forms
from .models import Student  # Import the Member model

class MemberForm(forms.ModelForm):
    class Meta:
        model = Student  # Specify the model to use
        fields = '__all__'  # Use all fields from the model

        # Add custom labels for form fields
        labels = {
            'name': 'Type Your Name',  # Label for the 'name' field
            'email': 'Enter Email-Address',  # Label for the 'age' field
            'course': 'Course Name',  # Label for the 'age' field
        }

        # Optionally, add help texts or widgets if needed
        help_texts = {
            'name': 'Enter your full name here.',
        }