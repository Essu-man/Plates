from django.shortcuts import redirect, render

from .forms import InvoiceForm


def upload_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Replace with your success URL
    else:
        form = InvoiceForm()
    return render(request, 'upload_invoice.html', {'form': form})
