from django.core.management.base import BaseCommand
from pruefung.models import Art

class Command(BaseCommand):
    help = "Grundsätzliche Arten Von Prüfungen hinzufügen"
    
    def handle(self, *args, **kwargs):
        arten = ["Sichtprüfung", "Sicht und Funktionsprüfung", "5 Jahresprüfung"]
        
        for art_name in arten:
            obj, created = Art.objects.get_or_create(name=art_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ "{obj.name}" hinzugefügt!'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️ "{obj.name}" existiert bereits!'))
        
