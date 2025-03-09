import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geraeteverwaltung.settings')
django.setup()

from geraete.models import Geraet, Kategorie
from django.db.models import Q

def import_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            # Kategorie sicherstellen
            kategorie, created = Kategorie.objects.get_or_create(
                name=row['Typ']
            )
            # Gerät erstellen oder aktualisieren
            barcode = row['Barcode'] if row['Barcode'] else None
            identifikation = row['Identifikation']
            inventarnummer = row['Inventarnummer']

            # Überprüfen, ob ein Gerät mit derselben Identifikation oder Barcode existiert
            geraet = Geraet.objects.filter(
                Q(identifikation=identifikation) | Q(barcode=barcode)
            ).first()

            if geraet:
                # Gerät aktualisieren
                geraet.kategorie = kategorie
                geraet.inventarnummer = inventarnummer
                geraet.barcode = barcode
                geraet.save()
            else:
                # Neues Gerät erstellen
                Geraet.objects.create(
                    identifikation=identifikation,
                    kategorie=kategorie,
                    inventarnummer=inventarnummer,
                    barcode=barcode,
                )

if __name__ == '__main__':
    file_path = r'C:\Users\Arne\Documents\Django\geraeteverwaltung\geraete.csv'
    import_csv(file_path)
    print('Data imported')