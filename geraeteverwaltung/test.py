from django.test import TestCase, Client
from django.urls import reverse
from geraete.models import Geraet, Status, Kategorie
from pruefung.models import Pruefung, Art, Checkliste_Ergebnis, Checkliste_Fragen, Befund
from datetime import date

class PruefungModelTest(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name='Einsatzbereit')
        self.kategorie = Kategorie.objects.create(name='Zurrgurt')
        self.geraet = Geraet.objects.create(
            bezeichnung='Ergolash Zurrgurt 0,5m',
            identifikation='Zurrgurt 10-48-2 01',
            seriennummer='54321',
            hersteller='Testhersteller',
            kaufdatum='2021-01-01',
            status=self.status,
            kategorie=self.kategorie,
            bemerkung='Testbemerkung',
            barcode=12345
        )
        self.befund = Befund.objects.create(name='Einsatzbereit')
        self.art = Art.objects.create(name='Sichtprüfung')
        self.pruefung = Pruefung.objects.create(
            geraet=self.geraet,
            art=self.art,
            befund=self.befund,
            intervall=12,
            pruefer='A. Dusenka',
            datum=date(2021, 1, 1),
            bemerkung='Testbemerkung',
            bestanden = True,
        )
        self.checkliste_fragen = Checkliste_Fragen.objects.create(
            frage='Testfrage',
            art=self.art,
            kategorie=self.kategorie
        )
        self.checkliste_ergebnis = Checkliste_Ergebnis.objects.create(
            pruefung=self.pruefung,
            frage=self.checkliste_fragen,
            antwort=True,
            bemerkung='Testantwort'
        )
        
    def test_geraet_str(self):
        self.assertEqual(str(self.geraet), 'Ergolash Zurrgurt 0,5m (Zurrgurt 10-48-2 01)')

    def test_status_str(self):
        self.assertEqual(str(self.status), 'Einsatzbereit')

    def test_kategorie_str(self):
        self.assertEqual(str(self.kategorie), 'Zurrgurt')

    def test_pruefung_str(self):
        self.assertEqual(str(self.pruefung), 'Ergolash Zurrgurt 0,5m (Zurrgurt 10-48-2 01) wurde am 2021-01-01 geprüft')

    def test_art_str(self):
        self.assertEqual(str(self.art), 'Sichtprüfung')

    def test_checkliste_fragen_str(self):
        self.assertEqual(str(self.checkliste_fragen), 'Testfrage')

    def test_checkliste_ergebnis_str(self):
        self.assertEqual(str(self.checkliste_ergebnis), 'Ergolash Zurrgurt 0,5m (Zurrgurt 10-48-2 01) Frage: Testfrage')
        
    def test_nachste_pruefung(self):
        self.assertEqual(self.pruefung.naechste_pruefung(), date(2022, 1, 1))