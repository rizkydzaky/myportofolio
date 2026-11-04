from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse,  QueryDict
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/index.html", {"contacts": contacts})

def contact_add(request):
    if request.method == "POST":
        contact = Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
        )

        response = render(
            request,
            "contacts/_contact_add_response.html",
            {"contact": contact},
        )

        response.content += b'''
        <div id="feedback" hx-swap-oob="true">
            Kontak berhasil ditambahkan!
        </div>
        '''

        return response

    return HttpResponse("")

@require_http_methods(["DELETE"])
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return HttpResponse("")

def contact_search(request):
    query = request.GET.get("q", "")

    if query:
        contacts = Contact.objects.filter(name__icontains=query)
    else:
        contacts = Contact.objects.all()

    return render(
        request,
        "contacts/_contact_rows.html",
        {"contacts": contacts},
    )

def contact_search(request):
    query = request.GET.get("q", "")

    if query:
        contacts = Contact.objects.filter(name__icontains=query)
    else:
        contacts = Contact.objects.all()

    return render(
        request,
        "contacts/_contact_rows.html",
        {"contacts": contacts},
    )

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    return render(
        request,
        "contacts/_contact_edit_row.html",
        {"contact": contact},
    )

def contact_row(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    return render(
        request,
        "contacts/_contact_row.html",
        {"contact": contact},
    )

@require_http_methods(["PUT"])
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    data = QueryDict(request.body)

    contact.name = data.get("name", contact.name)
    contact.email = data.get("email", contact.email)
    contact.phone = data.get("phone", contact.phone)
    contact.save()

    return render(
        request,
        "contacts/_contact_row.html",
        {"contact": contact},
    )