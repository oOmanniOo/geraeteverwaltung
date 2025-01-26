# Geräteverwaltung

Dieses Projekt ist eine auf Django basierende Webanwendung zur Verwaltung von Geräten. Es ermöglicht Benutzern, Geräteinformationen hinzuzufügen, zu aktualisieren und zu löschen sowie eine Liste aller Geräte anzuzeigen.

## Funktionen

- Neue Geräte mit Details wie Name, Typ und Seriennummer hinzufügen.
- Bestehende Geräteinformationen aktualisieren.
- Geräte aus dem System löschen.
- Eine Liste aller Geräte mit ihren Details anzeigen.

## Installation

1. Repository klonen:
    ```bash
    git clone https://github.com/yourusername/geraeteverwaltung.git
    ```
2. In das Projektverzeichnis wechseln:
    ```bash
    cd geraeteverwaltung
    ```
3. Erforderliche Abhängigkeiten installieren:
    ```bash
    pip install -r requirements.txt
    ```
4. Migrationen anwenden:
    ```bash
    python manage.py migrate
    ```
5. Entwicklungsserver starten:
    ```bash
    python manage.py runserver
    ```

## Nutzung

1. Öffnen Sie Ihren Webbrowser und gehen Sie zu `http://127.0.0.1:8000/`.
2. Verwenden Sie die Schnittstelle, um Ihre Geräte zu verwalten.

## Beitrag

Beiträge sind willkommen! Bitte forken Sie das Repository und senden Sie eine Pull-Anfrage.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.