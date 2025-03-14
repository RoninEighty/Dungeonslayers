import csv
import os

def tabelle(länge, wert):
    md_datei.write("| " + wert)
    # X Leerzeichen, Minus die Anzahl der Zahlen
    länge = länge - len(wert)
    länge = länge + 1
    durchlauf = 0
    while durchlauf < länge:
        md_datei.write(" ")
        länge = länge - 1

#Ersetze Klassen Abkürzungen durch Namen
def klassen():
    if zeile[4] == "ATT":
        md_datei.write('- Klasse: Attentäter  \n')
    elif zeile[4] == "BER":
        md_datei.write('- Klasse: Beserker  \n')
    elif zeile[4] == "BLU":
        md_datei.write('- Klasse: Blutmagier  \n')
    elif zeile[4] == "DÄM":
        md_datei.write('- Klasse: Dämonologe  \n')
    elif zeile[4] == "ELE":
        md_datei.write('- Klasse: Elementarist  \n')
    elif zeile[4] == "Hei":
        md_datei.write('- Klasse: Heiler  \n')
    elif zeile[4] == "KRI":
        md_datei.write('- Klasse: Krieger  \n')
    elif zeile[4] == "KRZ":
        md_datei.write('- Klasse: Kriegszauberer  \n')
    elif zeile[4] == "NEK":
        md_datei.write('- Klasse: Nekromant  \n')
    elif zeile[4] == "PAL":
        md_datei.write('- Klasse: Paladin  \n')
    elif zeile[4] == "Sch":
        md_datei.write('- Klasse: Schwarzmagier  \n')
    elif zeile[4] == "BER":
        md_datei.write('- Klasse: Beserker  \n')
    elif zeile[4] == "SPÄ":
        md_datei.write('- Klasse: Späher  \n')
    elif zeile[4] == "WAM":
        md_datei.write('- Klasse: Waffenmeister  \n')
    elif zeile[4] == "Zau":
        md_datei.write('- Klasse: Zauberer  \n')

#Ersetze Sonderzeichen, Leerzeichen in Strings
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

# Pfad zur CSV-Datei
csv_datei = 'Bestiarium_Pit.csv'
csv_datei_translation = 'slayerspit_translations.de.csv'
# Erstelle die Verzeichnisse, falls es nicht existiert
Test_output_verzeichnis_grw = 'bestiarium_grw'
Test_output_verzeichnis_fanwerk ='bestiarium_fanwerk'
os.makedirs(Test_output_verzeichnis_grw, exist_ok=True)
os.makedirs(Test_output_verzeichnis_fanwerk, exist_ok=True)

# Lese die Translation CSV-Datei und schreibe sie in eine Liste "thisList
with open(csv_datei_translation, mode='r', encoding='utf-8') as csv_datei_translation:
        csv_reader = csv.reader(csv_datei_translation, delimiter=',')
        # Dictionary wird erstellt
        werteDict = {
                }
        # Dictionary wird mit Inhalt von CSV Übersetzungstabelle gefüllt
        for zeile in csv_reader:
                werteDict[zeile[1]] = zeile[2]

# Lese die Bestiariums CSV-Datei und schreibe die Markdown-Dateien
with open(csv_datei, mode='r', encoding='utf-8') as csv_datei:
    csv_reader = csv.reader(csv_datei, delimiter=',')
    
    for zeile in csv_reader:
        print(f'Name: {zeile[0]}')
 
        # Erstelle Datei
        dateiname = replace(zeile[0])
        dateiname = dateiname + '.md' # Dateiname aus der ersten Spalte

        # Verzeichnis für Grundregelwerk oder Fanwerk
        if zeile[1] == "Dungeonslayers Basisbox":
            dateipfad = os.path.join(Test_output_verzeichnis_grw, dateiname)
        else:
            dateipfad = os.path.join(Test_output_verzeichnis_fanwerk, dateiname)    
 
        # Schreibe die Zeile in die Markdown-Datei
        with open(dateipfad, mode='w', encoding='utf-8') as md_datei:
            md_datei.write('# ' + zeile[0] + '  \n')
            md_datei.write('- Gruppe: ' + zeile[2] + '  \n')
            if zeile[3]:
                md_datei.write('- Volk: ' + zeile[3] + '  \n')
            if zeile[4]:
                klassen()
            if zeile[5]:
                md_datei.write('- Stufe: ' + zeile[5] + '  \n')
            if zeile[6]:
                md_datei.write('- Fähigkeiten: ' + zeile[6] + '  \n\n')
            if zeile[7]:
                md_datei.write('- Upgrade: ' + zeile[7] + '  \n')
            md_datei.write("\n")

            # Attribute
            md_datei.write('| KÖR | AGI | GEI |  \n')
            md_datei.write('| --- | --- | --- |  \n')            
            # Körper - Zeile 8
            tabelle(3, zeile[8])
            # Agilität - Zeile 9
            tabelle(3, zeile[9])
            # Geist - Zeile 10
            tabelle(3, zeile[10])
            md_datei.write("|\n")
            md_datei.write('| ST  | BE  | VE  |  \n')
            # Stärke - Zeile 11
            tabelle(3, zeile[11])
            # Beweglichkeit - Zeile 12
            tabelle(3, zeile[12])
            # Verstand - Zeile 13
            tabelle(3, zeile[13])
            md_datei.write("|\n")
            md_datei.write('| HÄ  | GE  | AU  |  \n')
            # Härte Zeile 14
            tabelle(3, zeile[14])
            # Geschicklichkeit - Zeile 15
            tabelle(3, zeile[15])
            # Aura - Zeile 16
            tabelle(3, zeile[16])
            md_datei.write("|\n")
            md_datei.write('\n\n')

            
            # Kampfwerte
            md_datei.write("| Leben    | Abwehr   | Initiative | Laufen     |\n")
            md_datei.write("| -------- | -------- | ---------- | ---------- |\n")
            # Zeile 17 - Lebenskraft
            tabelle(8, zeile[17])
            # Zeile 20 - Abwehr
            tabelle(8, zeile[20])
            # Zeile 18 - Initiative
            tabelle(10, zeile[18])
            # Zeile 19 - Laufen
            tabelle(10, zeile[19])
            md_datei.write("|\n")
            md_datei.write("| Schlagen | Schießen | Zaubern    | Zielzauber |\n")
#            md_datei.write("| -------- | -------- | ---------- | ---------- |\n")
            # Zeile 21 - Schlagen
            tabelle(8, zeile[21])
            # Zeile 22 - Schießen
            tabelle(8, zeile[22])
            # Zeile 23 - Zauber
            tabelle(10, zeile[23])
            # Zeile 24 - Zielzauber
            tabelle(10, zeile[24])
            md_datei.write("|\n\n")

            # Zeile 30 - Waffen
            md_datei.write("**Bewaffnung:**  \n")
            md_datei.write(zeile[30] + "\n\n")

            # Zeile 31 - Panzerung
            md_datei.write("**Panzerung:**  \n")
            md_datei.write(zeile[31] + "\n\n")

            # Zeile 31 - Ausrüstung
            if zeile[31]:
                md_datei.write("**Ausrüstung:**  \n")
                md_datei.write(zeile[31] + "\n\n")

            # Zeile 29 - Talente
            md_datei.write("**Talente:**  \n")
            # Die Talenzeile wird aufgeteil und in eine Liste geschrieben
            saetze = zeile[29].split(", ")            
            for zeileSaetze in saetze:
                words = zeileSaetze.split()
                # Schreibe Liste in die Markdown-Datei
                for zeileWords in words:
                        zeileWords = zeileWords.replace(",", "")
                        # Wenn der String in der Übersetzungstabelle gefunden wird, wird das Wort ersetzt
                        if None != werteDict.get(zeileWords):
                                md_datei.write(werteDict.get(zeileWords) + ' ')
                        else:
                                md_datei.write(zeileWords + ' ')
                md_datei.write("\n\n")
            md_datei.write("\n")

            # Zeile 33 - Zaubersprüche
            if zeile[33]:
                md_datei.write("**Zaubersprüche:**  \n")
                md_datei.write(zeile[33] + "\n\n")

            # Zeile 25 - Gegnerhärte
            md_datei.write("Gegnerhärte: " + zeile[25] + "  \n")
            
            # Zeile 26 - Größe
            if zeile[26] == "wi":
                md_datei.write("Größe: Winzig  \n")
            elif zeile[26] == "kl":
                md_datei.write("Größe: Klein  \n")
            elif zeile[26] == "no":
                md_datei.write("Größe: Normal  \n")
            elif zeile[26] == "gr":
                md_datei.write("Größe: Groß  \n")
            elif zeile[26] == "ri":
                md_datei.write("Größe: Riesig  \n")
            elif zeile[26] == "ge":
                md_datei.write("Größe: ge  \n")

            # Zeile 27 - Erfahrungspunkte
            md_datei.write("Erfahrungspunkte: " + zeile[27] + "  \n")

          


            # Footers
            md_datei.write('\n\n\n')
            md_datei.write('___\n')
            md_datei.write('*Fanwerk für [Dungeonslayers](https://www.dungeonslayers.net/) (C) Christian Kennig | ')
            md_datei.write('Quelle: ' + zeile[1] + ' | ')
            md_datei.write('Lizenz: [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de)*')

