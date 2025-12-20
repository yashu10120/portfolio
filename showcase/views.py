from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact   # import your model

def portfolio(request):
    return render(request, "portfolio.html")

def about(request):
    return render(request, "about.html")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # saves to database
            messages.success(request, "Your message has been sent successfully!")
            return redirect("portfolio")  # ✅ redirect back to portfolio page
    else:
        form = ContactForm()
    return render(request, "portfolio.html", {"form": form})

def entries_view(request):
    # ✅ properly formatted
    contacts = Contact.objects.all().order_by("-created_at")
    return render(request, "entries.html", {"contacts": contacts})

def success_view(request):
    return render(request, "success.html")
