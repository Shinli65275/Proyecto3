from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .foms import LibroForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/formulario.html', {'form': form})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    form = LibroForm(request.POST or None, instance=libro)
    if form.is_valid():
        form.save()
        return redirect('lista_libros')
    return render(request, 'biblioteca/formulario.html', {'form': form})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'biblioteca/eliminar.html', {'libro': libro})


def generar_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="libros.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 12)

    y = 800
    p.drawString(50, y, "Reporte de Libros")
    y -= 30

    libros = Libro.objects.all()
    for libro in libros:
        texto = f"{libro.titulo} - {libro.autor}"
        p.drawString(50, y, texto)
        y -= 20

    p.showPage()
    p.save()
    return response