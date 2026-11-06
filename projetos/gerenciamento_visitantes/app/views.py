from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms.create_visitor_form import CreateVisitorForm
from .forms.update_visitor_form import UpdateVisitorForm
from .models import Visitor, TicketType
from datetime import datetime
from uuid import uuid4

# Create your views here.
def home(request):
    return render(request, 'home.html')

def visitors(request):
    search = request.GET.get('name_or_cpf' , '')
    ticket_type = request.GET.get('ticket_type', '0')
    ticket_date = request.GET.get('ticket_date', '')
    ordering = request.GET.get('ordering', '1')
    if ordering not in {'1', '2'}:
        ordering = '1'

    visitors = Visitor.objects.all()

    visitors = visitors.filter(
        Q(first_name__icontains=search) 
        | Q(last_name__icontains=search)
        | Q(cpf__contains=search)
    )

    valid_types = {str(value) for value in TicketType.values}

    ticket_type_int = int(ticket_type)
    if ticket_type in valid_types:
       visitors = visitors.filter(ticket_type=ticket_type_int)

    if ticket_date:
        try:
            ticket_date_filter = datetime.strptime(ticket_date, '%Y-%m-%d').date()
        except ValueError:
            ticket_date = ''
        else:
            visitors = visitors.filter(ticket_date=ticket_date_filter)

    if ordering == '2':
        today = timezone.localdate()
        visitors = sorted(
            visitors,
            key=lambda visitor: (
                today.year - visitor.birth_date.year
                - ((today.month, today.day) < (visitor.birth_date.month, visitor.birth_date.day)),
                visitor.first_name.casefold(),
                visitor.last_name.casefold(),
            ),
        )
    else:
        visitors = visitors.order_by('first_name', 'last_name')
        


    response = {
        'visitors': visitors,
        'search': search,
        'ticket_type': ticket_type_int,
        'ticket_date': ticket_date,
        'ordering': int(ordering),
    }

    return render(request, 'visitors.html', response)

def create_visitor(request):
    if request.method == 'POST':
        visitor_forms = CreateVisitorForm(request.POST)

        if visitor_forms.is_valid():
            visitor = visitor_forms.save(commit=False)
            visitor.ticket_number = str(uuid4())
            visitor.save()

            return redirect('visitors')

    else:
        visitor_forms = CreateVisitorForm()

    response = {
        'form' : visitor_forms
    }

# cpf = request.POST['cpf']
# if Visitor.objects.filter(cpf=cpf).exists():
#     return render(request, 'create-visitor.html', {
#                 'error': 'Já existe um visitante cadastrado com este CPF.',
#                 'form_data': request.POST,
#             })

# ticket_date = datetime.strptime(request.POST['ticket_date'], '%Y-%m-%d').date()
# if ticket_date < timezone.localdate():
#     return render(request, 'create-visitor.html', {
#                 'error': 'A data do ingresso não pode ser anterior à data atual.',
#                 'form_data': request.POST,
#             })

    return render(request, 'create-visitor.html', response)


        

def update_visitor(request, id):
    visitor = Visitor.objects.get(pk=id)


    if request.method == 'POST':
        visitor_form = UpdateVisitorForm(request.POST, instance=visitor)
       
       
        if visitor_form.is_valid():
            visitor_form.save()
            return redirect('visitors')

    else:
        visitor_form = UpdateVisitorForm(instance=visitor)

    response = {
        'visitor': visitor,
        'form': visitor_form
    }

    return render(request, 'update-visitor.html', response)
        # cpf = request.POST['cpf']

        # if Visitor.objects.filter(cpf=cpf).exclude(pk=visitor.pk).exists():
        #     return render(request, 'update-visitor.html', {
        #         'visitor': visitor,
        #         'error': 'Já existe um visitante cadastrado com este CPF.',
        #     })

        # ticket_date = datetime.strptime(request.POST['ticket_date'], '%Y-%m-%d').date()
        # if ticket_date < timezone.localdate():
        #     return render(request, 'update-visitor.html', {
        #         'visitor': visitor,
        #         'error': 'A data do ingresso não pode ser anterior à data atual.',
        #     })

       

    

    

def delete_visitor(request, id):
    visitor = Visitor.objects.get(pk=id)
    visitor.delete()

    return redirect('visitors')


def estatisticas(request):
    ticket_counts = Visitor.objects.aggregate(
        total=Count('id'),
        normal=Count('id', filter=Q(ticket_type=TicketType.NORMAL)),
        vip=Count('id', filter=Q(ticket_type=TicketType.VIP)),
        premium=Count('id', filter=Q(ticket_type=TicketType.PREMIUM)),
    )

    today = timezone.localdate()
    ages = [
        today.year - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
        for birth_date in Visitor.objects.values_list('birth_date', flat=True)
    ]

    context = {
        'total_visitors': ticket_counts['total'],
        'normal_tickets': ticket_counts['normal'],
        'vip_tickets': ticket_counts['vip'],
        'premium_tickets': ticket_counts['premium'],
        'average_age': round(sum(ages) / len(ages), 1) if ages else 0,
    }
    return render(request, 'estatisticas.html', context)



    
