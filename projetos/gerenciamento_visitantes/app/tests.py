from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import TicketType, Visitor


class StatisticsViewTests(TestCase):
    def test_statistics_show_visitor_and_ticket_counts_and_average_age(self):
        today = timezone.localdate()
        for age, ticket_type in (
            (10, TicketType.NORMAL),
            (20, TicketType.VIP),
            (30, TicketType.PREMIUM),
        ):
            Visitor.objects.create(
                first_name='Visitor',
                last_name=str(age),
                cpf=str(age).zfill(11),
                birth_date=date(today.year - age, today.month, today.day),
                ticket_date=today,
                ticket_type=ticket_type,
                ticket_number=f'ticket-{age}',
            )

        response = self.client.get(reverse('estatisticas_visitor'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_visitors'], 3)
        self.assertEqual(response.context['normal_tickets'], 1)
        self.assertEqual(response.context['vip_tickets'], 1)
        self.assertEqual(response.context['premium_tickets'], 1)
        self.assertEqual(response.context['average_age'], 20)
        self.assertContains(response, '20.0 anos')

    def test_statistics_show_zeroes_when_there_are_no_visitors(self):
        response = self.client.get(reverse('estatisticas_visitor'))

        self.assertEqual(response.context['total_visitors'], 0)
        self.assertEqual(response.context['average_age'], 0)
        self.assertContains(response, '0 anos')


class VisitorViewTests(TestCase):
    def create_visitor(self, first_name, cpf, birth_date):
        return Visitor.objects.create(
            first_name=first_name,
            last_name='Visitor',
            cpf=cpf,
            birth_date=birth_date,
            ticket_date=timezone.localdate(),
            ticket_type=TicketType.NORMAL,
            ticket_number=f'ticket-{cpf}',
        )

    def test_create_rejects_an_existing_cpf_and_keeps_form_data(self):
        today = timezone.localdate()
        self.create_visitor('Existing', '12345678901', date(1990, 1, 1))

        response = self.client.post(reverse('create_visitor'), {
            'first_name': 'New',
            'last_name': 'Visitor',
            'cpf': '12345678901',
            'birth_date': '2000-01-01',
            'ticket_date': today.isoformat(),
            'ticket_type': str(TicketType.NORMAL),
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Já existe um visitante cadastrado com este CPF.')
        self.assertContains(response, 'value="New"')
        self.assertEqual(Visitor.objects.count(), 1)

    def test_create_rejects_a_ticket_date_before_today(self):
        yesterday = timezone.localdate() - timedelta(days=1)

        response = self.client.post(reverse('create_visitor'), {
            'first_name': 'New',
            'last_name': 'Visitor',
            'cpf': '12345678901',
            'birth_date': '2000-01-01',
            'ticket_date': yesterday.isoformat(),
            'ticket_type': str(TicketType.NORMAL),
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A data do ingresso não pode ser anterior à data atual.')
        self.assertContains(response, f'value="{yesterday.isoformat()}"')
        self.assertEqual(Visitor.objects.count(), 0)

    def test_update_rejects_a_ticket_date_before_today(self):
        visitor = self.create_visitor('Existing', '12345678901', date(1990, 1, 1))
        yesterday = timezone.localdate() - timedelta(days=1)

        response = self.client.post(reverse('update_visitor', args=[visitor.pk]), {
            'first_name': 'Updated',
            'last_name': 'Visitor',
            'cpf': visitor.cpf,
            'birth_date': '2000-01-01',
            'ticket_date': yesterday.isoformat(),
            'ticket_type': str(TicketType.NORMAL),
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A data do ingresso não pode ser anterior à data atual.')
        visitor.refresh_from_db()
        self.assertEqual(visitor.ticket_date, timezone.localdate())

    def test_update_rejects_another_visitors_cpf(self):
        first = self.create_visitor('First', '12345678901', date(1990, 1, 1))
        second = self.create_visitor('Second', '10987654321', date(2000, 1, 1))

        response = self.client.post(reverse('update_visitor', args=[second.pk]), {
            'first_name': 'Updated',
            'last_name': 'Visitor',
            'cpf': first.cpf,
            'birth_date': '2000-01-01',
            'ticket_date': timezone.localdate().isoformat(),
            'ticket_type': str(TicketType.NORMAL),
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Já existe um visitante cadastrado com este CPF.')
        second.refresh_from_db()
        self.assertEqual(second.cpf, '10987654321')

    def test_visitors_can_be_sorted_by_name_or_current_age(self):
        today = timezone.localdate()
        younger_date = date(today.year - 20, today.month, today.day)
        older_date = date(today.year - 30, today.month, today.day)
        self.create_visitor('Zoe', '00000000001', younger_date)
        self.create_visitor('Amy', '00000000002', older_date)

        name_response = self.client.get(reverse('visitors'), {'ordering': '1'})
        age_response = self.client.get(reverse('visitors'), {'ordering': '2'})

        self.assertEqual(
            [visitor.first_name for visitor in name_response.context['visitors']],
            ['Amy', 'Zoe'],
        )
        self.assertEqual(
            [visitor.first_name for visitor in age_response.context['visitors']],
            ['Zoe', 'Amy'],
        )

    def test_visitors_can_be_filtered_by_ticket_date(self):
        today = timezone.localdate()
        tomorrow = today + timedelta(days=1)
        matching = self.create_visitor('Matching', '00000000001', date(1990, 1, 1))
        matching.ticket_date = tomorrow
        matching.save()
        self.create_visitor('Other', '00000000002', date(1990, 1, 1))

        response = self.client.get(reverse('visitors'), {'ticket_date': tomorrow.isoformat()})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['visitors']), [matching])
        self.assertContains(response, 'value="' + tomorrow.isoformat() + '"')
