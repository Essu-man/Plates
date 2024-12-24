from django.contrib.auth.decorators import LoginView
from django.shortcuts import redirect, render

from .forms import InvoiceForm


class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return '/dashboard/'

def upload_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Replace with your success URL
    else:
        form = InvoiceForm()
    return render(request, 'upload_invoice.html', {'form': form})
