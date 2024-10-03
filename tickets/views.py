from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from django.contrib.auth.decorators import login_required

@login_required
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        ticket = Ticket(title=title, description=description, created_by=request.user)
        ticket.save()
        return redirect('ticket_list')
    return render(request, 'create_ticket.html') 


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})


@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        ticket.title = request.POST['title']
        ticket.description = request.POST['description']
        ticket.status = request.POST['status']
        ticket.save()
        return redirect('ticket_list')
    return render(request, 'update_ticket.html', {'ticket': ticket})