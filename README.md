Geräteverwaltung & Prüfungsmanagement
Dieses Projekt ist eine Django-basierte Anwendung zur Verwaltung von Geräten und deren regelmäßiger Prüfung – speziell zugeschnitten auf die Anforderungen einer Feuerwehr. Es umfasst Funktionen zur Geräteverwaltung, zur Planung und Nachverfolgung von Prüfungen (Prüfungen) sowie zur Durchführung von Checklisten während der Prüfungen gemäß DGUV Grundsatz 305-002.

Features
Geräteverwaltung: Erstellen, Bearbeiten und Löschen von Geräten mit detaillierten Attributen.
Prüfungsmanagement: Planung und Nachverfolgung von Prüfungen; automatische Berechnung des nächsten Prüftermins anhand eines konfigurierbaren Intervalls.
Checklisten: Dynamische Checklisten, die während einer Prüfung basierend auf der Prüfungsart und dem Gerätetyp generiert werden. Die Ergebnisse werden zusammen mit der Prüfung in der Datenbank gespeichert.
Automatische Statusaktualisierung: Beim Speichern einer Prüfung wird automatisch über Django-Signals (oder alternativ in der View) ein separater Eintrag aktualisiert, der für jedes Gerät und jede Prüfungsart das Datum der letzten und der nächsten Prüfung speichert.
Admin-Interface: Verwaltung aller Modelle über das integrierte Django-Admin.
Benutzerbenachrichtigungen: Einsatz des Django-Nachrichtenframeworks, um Rückmeldungen (z. B. "Prüfung erfolgreich durchgeführt") an den Benutzer zu übermitteln.
Live-Testumgebung: Möglichkeit, die Anwendung in einer produktionsähnlichen Umgebung auf einem Windows-PC mit SQLite3 laufen zu lassen.
Installation
Voraussetzungen
Python 3.10 (oder höher)
Git
Eine virtuelle Umgebung (z. B. venv)
Schritt-für-Schritt-Anleitung
Repository klonen

Öffne ein Terminal und klone das Repository:

git clone https://github.com/dein-benutzername/gerateverwaltung.git
cd gerateverwaltung
Virtuelle Umgebung erstellen und aktivieren

Erstelle und aktiviere eine virtuelle Umgebung:

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
Abhängigkeiten installieren

Installiere alle benötigten Pakete:

pip install -r requirements.txt
Umgebungsvariablen konfigurieren

Erstelle eine .env-Datei im Projektstamm (dort, wo auch manage.py liegt) und trage die nötigen Variablen ein, z. B.:

env
Kopieren
Bearbeiten
SECRET_KEY=dein_geheimer_schluessel
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
Datenbank migrieren

Erstelle die Datenbank und führe die Migrationen aus:

python manage.py makemigrations
python manage.py migrate
Statische Dateien sammeln

Sammle alle statischen Dateien:

Bearbeiten
python manage.py collectstatic --noinput
Admin-Benutzer erstellen

Erstelle einen Superuser, um Zugriff auf das Admin-Panel zu erhalten:

python manage.py createsuperuser
Testserver starten

Starte den Entwicklungsserver:

Bearbeiten
python manage.py runserver
Die Anwendung ist dann unter http://127.0.0.1:8000 erreichbar.

Nutzung
Geräteverwaltung:
Gehe zur URL /geraete/, um alle Geräte zu verwalten.

Prüfungsmanagement:

Wähle unter /pruefung/auswahl/ die gewünschte Prüfungsart und das Gerät aus.
Fülle im Formular unter /pruefung/durchfuehren/ die Prüfungsdaten sowie die zugehörige Checkliste aus.
Nach erfolgreichem Speichern erhältst du eine Bestätigung und kannst die Prüfungsergebnisse in der Übersicht einsehen.
Admin-Interface:
Über http://127.0.0.1:8000/admin/ können alle Daten (Geräte, Prüfungen, Checklisten) verwaltet werden.

Deployment (Live-Testumgebung)
Das Projekt kann auch in einer produktionsähnlichen Umgebung auf einem Windows-PC ausgeführt werden. Die Schritte sind im Grunde identisch mit der Installation:

Repository klonen und virtuelle Umgebung einrichten
Abhängigkeiten installieren
Umgebungsvariablen konfigurieren (setze DEBUG=False in der Produktion)
Migrationen ausführen und statische Dateien sammeln
Einen Produktionsserver starten
Für eine lokale Produktionsumgebung kannst du z. B. Waitress verwenden:

bash
Kopieren
Bearbeiten
waitress-serve --port=8000 geraeteverwaltung.wsgi:application
Stelle sicher, dass die Firewall den Port 8000 freigibt, damit die Anwendung im Netzwerk erreichbar ist.

Contributing
Beiträge sind willkommen! Wenn du Fehler findest oder neue Features hinzufügen möchtest, erstelle bitte einen Issue oder pull request.

