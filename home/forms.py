from django import forms


import decimal

class WorkScheduleForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Please enter your name', 'required': True}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your city', 'required': True}))
    work_details = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Describe your work details in detail', 'required': True}))
    pin_code = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Enter your pin code', 'required': True}))
    nearest_location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nearest location', 'required': True}))
    complexity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Work complexity 1 to 10', 'min': 1, 'max': 10, 'required': True}))
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'placeholder': 'Date', 'required': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'required': True}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'required': True}))
    alternate_contact_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Alternate contact number (optional)'}))
    preferred_contact_time = forms.TimeField(required=False, widget=forms.TimeInput(attrs={'type': 'time', 'placeholder': 'Preferred contact time'}))
    service_type = forms.ChoiceField(choices=[
        ('electrician', 'Electrician'),
        ('plumber', 'Plumber'),
        ('carpenter', 'Carpenter'),
        ('painter', 'Painter'),
        ('handyman', 'Handyman'),
        ('appliance_repair', 'Appliance Repair Technician'),
        ('landscaper', 'Landscaper/Gardener'),
        ('cleaner', 'House Cleaner'),
        ('roofer', 'Roofing Specialist'),
        ('interior_designer', 'Interior Designer/Decorator')
    ], widget=forms.Select(attrs={'placeholder': 'Select service type', 'required': True}))
    preferred_technician = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Preferred technician (if any)'}))
    gender_preference = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'Technician gender preference (if any)'}))
    special_instructions = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Special instructions'}))
    budget_range = forms.DecimalField(max_digits=10, decimal_places=2, required=False, widget=forms.NumberInput(attrs={'placeholder': 'Budget range', 'step': '0.01'}))
    attachments = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'placeholder': 'Upload related images/documents'}))
    customer_type = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Customer type (new/returning)', 'required': True}))
    referral_code = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Referral code (if any)'}))

    def clean_budget_range(self):
        budget_range = self.cleaned_data.get('budget_range')
        if isinstance(budget_range, decimal.Decimal):
            return str(budget_range)
        return budget_range