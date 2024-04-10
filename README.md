# LeistungsanalyseApp

## Vorbereitungen für das Programm

1. Ordner erstellen
2. die gegeben Datein: ```my_fuctions``` herunterladen und in den Ordner einfügen
3. .gitignore Datei erstellen um ünnotige Datein nicht mit hochzuladen
4. virtuelle Umgebung erstellen und benötigte Bibliotheken herunterladen
5. Hauptprogramm schreiben um den User nach den Daten zu fragen und diese in späterer folge auszuwerten

## Virtuelle Umgebung erstellen
Bezogen auf die Erstellung auf dem MacBook:
Die virtuelle Umgebung kann mithilfe der Kommandozeile erstellt werden, hierzu muss man den folgenden Befehl eingeben:

```python3 -m venv venv```

Anschließend muss diese Virtuelle Umgebung noch aktiviert werden, dies erfolgt durch den Befehl:

```source /venv/bin/activate```

Nun können innerhalb der virtuellen Umgebung alle Bibliotheken die gebraucht werden installiert werden ohne diese direkt auf dem PC zu haben.

Für dieses Projekt wird aktuell nur das Json-Modul gebraucht.

## Funktionsweise des Programms 

Das Hauptprogramm fragt den Benutzer nach den spezifischen Daten zu seinem Probanten/seiner Probantin, anschließend wird der Benutzer nach einem Namen 
für das Experiment gefragt und nach seinem/ihrem eigenen Namen. Diese Daten werden dann mit dem Json Modul in eine Datei gespeichert und kann anschließend vom Benutzer geöffnet werden und zur weiterverabreitung verwendet werden.



