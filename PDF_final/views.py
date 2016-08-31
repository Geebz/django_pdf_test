from django.shortcuts import render

# Create your views here.
from easy_pdf.views import PDFTemplateView

class HelloPDFView(PDFTemplateView):
    template_name = "PDF_final/hello.html"

def show(request):
    return render(request, 'PDF_final/hello.html', {})

