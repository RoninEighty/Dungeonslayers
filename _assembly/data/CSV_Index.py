import csv
import os

# Pfad zur CSV-Datei
csv_datei = 'Bestiarium.csv'

# Verzeichnis, in dem die Markdown-Dateien gespeichert werden sollen
output_verzeichnis = 'Output'
output_datei = 'index-bestiarium.md'

# Funktionen
def replace(string_replace):
        string_replace = string_replace.replace(" ", "-")
        string_replace = string_replace.replace("`", "-")
        string_replace = string_replace.replace("'", "")
        string_replace = string_replace.replace("(", "")
        string_replace = string_replace.replace(")", "")
        string_replace = string_replace.replace(",", "")
        string_replace = string_replace.replace('ä', 'ae')
        string_replace = string_replace.replace('ö', 'oe')
        string_replace = string_replace.replace('ü', 'ue')
        string_replace = string_replace.replace('Ä', 'ae')
        string_replace = string_replace.replace('Ö', 'oe')
        string_replace = string_replace.replace('Ü', 'ue')
        string_replace = string_replace.replace('A', 'a')
        string_replace = string_replace.replace('B', 'b')
        string_replace = string_replace.replace('C', 'c')
        string_replace = string_replace.replace('D', 'd')
        string_replace = string_replace.replace('E', 'e')
        string_replace = string_replace.replace('F', 'f')
        string_replace = string_replace.replace('G', 'g')
        string_replace = string_replace.replace('H', 'h')
        string_replace = string_replace.replace('I', 'i')
        string_replace = string_replace.replace('J', 'j')
        string_replace = string_replace.replace('K', 'k')
        string_replace = string_replace.replace('L', 'l')
        string_replace = string_replace.replace('M', 'm')
        string_replace = string_replace.replace('N', 'n')
        string_replace = string_replace.replace('O', 'o')
        string_replace = string_replace.replace('P', 'p')
        string_replace = string_replace.replace('Q', 'q')
        string_replace = string_replace.replace('R', 'r')
        string_replace = string_replace.replace('S', 's')
        string_replace = string_replace.replace('T', 't')
        string_replace = string_replace.replace('U', 'u')
        string_replace = string_replace.replace('V', 'v')
        string_replace = string_replace.replace('W', 'w')
        string_replace = string_replace.replace('X', 'x')
        string_replace = string_replace.replace('Y', 'y')
        string_replace = string_replace.replace('Z', 'z')
        return string_replace


# Erstelle das Verzeichnis, falls es nicht existiert
os.makedirs(output_verzeichnis, exist_ok=True)

# Lese die CSV-Datei und schreibe die Markdown-Dateien
with open(csv_datei, mode='r', encoding='utf-8') as datei:
    csv_reader = csv.reader(datei, delimiter=',')
    header = next(csv_reader) # Überspringe die Kopfzeile, falls vorhanden
    # Öffne Markdown Datei zum Schreibe in Output Datei
    with open(output_datei, mode='w') as mdfile:
        # Jede Zeile wird reingeschrieben
        for Zeile in csv_reader:
            dateiname = replace(Zeile[0])
            mdfile.write('[' + Zeile[0] +']')
            if Zeile[1] == "Dungeonslayers Basisbox":
                mdfile.write('(grw/bestiarium/' + dateiname +'.md)')
            else:
                mdfile.write('(fankwerk/bestiarium/' + dateiname +'.md)')    
            mdfile.write('<br>')
            mdfile.write('\n')
            print(Zeile[0])

print("Markdown-Dateien wurden erfolgreich erstellt!")


#for zeile in csv_reader:
#dateiname = zeile[0] + '.md' # Dateiname aus der ersten Spalte
#dateipfad = os.path.join(output_verzeichnis, dateiname)

# Schreibe die Zeile in die Markdown-Datei
#with open(dateipfad, mode='w', encoding='utf-8') as md_datei:
#md_datei.write('# ' + zeile[0] + '\n\n') # Beispiel für eine Überschrift
#md_datei.write('\n'.join(zeile[1:])) # Restliche Inhalte in die Datei schreiben



### Hinweise:
# 1. CSV-Datei: Stelle sicher, dass du den Pfad zur CSV-Datei (`deine_datei.csv`) anpasst.
# 2. Output-Verzeichnis: Das Skript erstellt ein Verzeichnis namens `markdown_dateien`, in dem die Markdown-Dateien gespeichert werden.
# 3. Dateinamen: Die Dateien werden nach dem Namen in der ersten Spalte benannt und erhalten die Endung `.md`.
# 4. Markdown-Inhalt: Das Skript fügt eine Überschrift aus der ersten Spalte hinzu und schreibt den Rest der Zeile darunter.
