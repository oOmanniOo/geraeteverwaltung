# Geräteverwaltung & Prüfungsmanagement

Dieses Projekt ist eine Django-basierte Anwendung zur Verwaltung von Geräten und deren regelmäßiger Prüfung – speziell zugeschnitten auf die Anforderungen einer Feuerwehr. Die Anwendung umfasst Funktionen zur Geräteverwaltung, zur Planung und Nachverfolgung von Prüfungen sowie zur Durchführung von Checklisten während der Prüfungen gemäß DGUV Grundsatz 305-002.

## Features

- **Geräteverwaltung:**  
  Erstellen, Bearbeiten und Löschen von Geräten mit detaillierten Attributen.

- **Prüfungsmanagement:**  
  Planung und Nachverfolgung von Prüfungen; automatische Berechnung des nächsten Prüftermins basierend auf einem konfigurierbaren Intervall.

- **Checklisten:**  
  Dynamische Checklisten, die während einer Prüfung basierend auf der Prüfungsart und dem Gerätetyp generiert werden. Die Ergebnisse werden zusammen mit der Prüfung in der Datenbank gespeichert.

- **Automatische Statusaktualisierung:**  
  Beim Speichern einer Prüfung wird über Django-Signals ein separater Eintrag aktualisiert, der für jedes Gerät und jede Prüfungsart das Datum der letzten und der nächsten Prüfung speichert.

- **Admin-Interface:**  
  Verwaltung aller Modelle über das integrierte Django-Admin.

- **Benutzerbenachrichtigungen:**  
  Einsatz des Django-Nachrichtenframeworks, um Rückmeldungen (z. B. "Prüfung erfolgreich durchgeführt") an den Benutzer zu übermitteln.

- **Live-Testumgebung:**  
  Möglichkeit, die Anwendung in einer produktionsähnlichen Umgebung auf einem Windows-PC mit SQLite3 auszuführen.

## Installation

### Voraussetzungen

- Python 3.10 (oder höher)
- Git
- Eine virtuelle Umgebung (z. B. `venv`)

### Schritt-für-Schritt-Anleitung

1. **Repository klonen**

   Öffne ein Terminal und klone das Repository:

   ```bash
   git clone https://github.com/dein-benutzername/gerateverwaltung.git
   cd gerateverwaltung
   ```

2. **Virtuelle Umgebung erstellen und aktivieren**

   Erstelle und aktiviere eine virtuelle Umgebung:

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Abhängigkeiten installieren**

   Installiere alle benötigten Pakete:

   ```bash
   pip install -r requirements.txt
   ```

4. **Umgebungsvariablen konfigurieren**

   Erstelle eine `.env`-Datei im Projektstamm (dort, wo auch `manage.py` liegt) und trage die nötigen Variablen ein, z. B.:

   ```env
   SECRET_KEY=dein_geheimer_schluessel
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Datenbank migrieren**

   Erstelle die Datenbank und führe die Migrationen aus:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Statische Dateien sammeln**

   ```bash
   python manage.py collectstatic
   ```

7. **Admin-Benutzer erstellen**

   Erstelle einen Superuser, um auf das Admin-Panel zugreifen zu können:

   ```bash
   python manage.py createsuperuser
   ```

8. **Testserver starten**

   Starte den Entwicklungsserver:

   ```bash
   python manage.py runserver
   ```

   Die Anwendung ist dann unter [http://127.0.0.1:8000](http://127.0.0.1:8000) erreichbar.

## Nutzung

### Geräteverwaltung

Rufe `/geraete/` auf, um alle Geräte zu verwalten.

### Prüfungsmanagement

- Gehe zur URL `/pruefung/auswahl/`, um die gewünschte Prüfungsart und das Gerät auszuwählen.
- Fülle im Formular auf `/pruefung/durchfuehren/` die Prüfungsdaten und die zugehörige Checkliste aus.
- Nach erfolgreichem Speichern erhältst du eine Bestätigung, und die Prüfungsergebnisse sind in der Übersicht sichtbar.

### Admin-Interface

Über [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) können alle Modelle (Geräte, Prüfungen, Checklisten) verwaltet werden.

## Deployment (Live-Testumgebung)

Das Projekt kann auch in einer produktionsähnlichen Umgebung auf einem Windows-PC mit SQLite3 ausgeführt werden. Die Schritte sind im Grunde identisch mit der Installation:

1. **Repository klonen und virtuelle Umgebung einrichten**
2. **Abhängigkeiten installieren und Umgebungsvariablen konfigurieren**
   - Setze in der Produktion `DEBUG=False`.
3. **Migrationen ausführen und statische Dateien sammeln**
4. **Starte den Produktionsserver**

Für eine lokale Produktionsumgebung kannst du beispielsweise [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/) verwenden:

```bash
waitress-serve --port=8000 geraeteverwaltung.wsgi:application
```

**Stelle sicher, dass deine Firewall den Port 8000 freigibt, damit die Anwendung im Netzwerk erreichbar ist.**

## Contributing

Beiträge sind willkommen! Wenn du Fehler findest oder neue Features hinzufügen möchtest, erstelle bitte einen Issue oder Pull Request.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz – siehe die [LICENSE](LICENSE)-Datei für Details.

## Kontakt

Für Fragen oder Anregungen kontaktiere bitte **Dein Name**.