from django.core.management.base import BaseCommand
from geraete.models import Kategorie

class Command(BaseCommand):
    help = "Grundsätzliche Arten Von Prüfungen hinzufügen"
    
    def handle(self, *args, **kwargs):
        kategorien = [
                    "Feuerwehrleine", 
                    "Steckleiter", 
                    "Schnittschutzausrüstung",
                    "Kanister aus PE",
                    "Werkzeug",
                    "Schläuche",
                    "Strahlrohre",
                    "Handlampe"
                    ]
        
        for kategorie_name in kategorien:
            obj, created = Kategorie.objects.get_or_create(name=kategorie_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ "{obj.name}" hinzugefügt!'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️ "{obj.name}" existiert bereits!'))