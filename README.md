# Dungeonslayers

[Dungeonslayers](https://dungeonslayers.net/) ist ein freies Pen & Paper Rollenspiel, entwickelt von **Christian Kennig**. Es ist lizensiert unter der Lizenz [CC BY-NC-SA 3.0 DE](https://creativecommons.org/licenses/by-nc-sa/3.0/de/deed.de). 

In diesem Repository sollen die unterschiedlichen Regeln aus dem Grundregelwerk, sowie aus unterschiedlichen Fanwerken gesammelt und in einheitlichem Format angeboten werden. Das Format ist Markdown.

Es handelt sich dabei um ein Fanprojekt. Die offizielle Dungeonslayers-Webpage ist unter dem Link [https://dungeonslayers.net/](https://dungeonslayers.net/) zu finden.

Die Markdown-Dateien bilden die Grundlage für das [DS4 SRD+](https://ronineighty.github.io/Dungeonslayers/).

## Metadaten

Wir benutzen [Front Matter](https://frontmatter.codes/) zur Erfassung von Metadaten.

## Regeln für Dateinamen

Um Inkompatibilitäten zwischen unterschiedlichen Betriebs- und Dateisysteme zu vermeiden und einen reibungslosen Buildprozess und Verlinkungen in URLs zu ermöglichen, dürfen Dateinamen nur **Kleinbuchstaben**, **Zahlen**, **Bindestriche** und **Punkte** enthalten. **Leerzeichen** werden durch **Bindestrich** (**-**) und Umlaute durch eine entsprechende ASCII-Darstellung, d.h.
 
 - Ä -> ae
 - ä -> ae
 - Ö -> oe
 - ö -> oe
 - Ü -> ue
 - ü -> ue
 - ß -> ss

Eine kompatibler Dateinamen entspricht etwa der Regexp ```[a-z0-9\-\.]*```.

Eine Ersetzungsregel mit Regexp könnte beispielsweise so aussehen, hier in Javascript:

    filename.toLowerCase() // Kleinbuchstaben
    .replace(/ü/g, 'ue') // Umlaute
    .replace(/ä/g, 'ae')
    .replace(/ö/g, 'oe')
    .replace(/ß/g, 'ss')
    .replace(/\s/g, '-') // Leerzeichen
    .replace(/[^a-z0-9\-\.]/ig, '') // Alle anderen Sonderzeichen raus

## Build: HTML-Seiten generieren

Unter ```_assembly``` finden sich die Vorlagen, Stile und Scripte um die Markdown Inhalte in eine HTML Struktur zu transformieren.
    
Der Prozess kann lokal auf einer Linux Shell ausgeführt werden.

    sh _assembly/scripts/make-html.sh

Die generierten HTML-Seiten finden sich anschliessend unter ```_site```.

### Softwareabhängigkeiten

```make-html.sh``` hat folgende Abhängigkeiten:

 - pandoc
 - perl
 - dos2unix
 - find
 - cut
 - cat
 - grep

Bitte stellt sicher, dass die entsprechenden Pakete auf eurem Linuxsystem vorhanden sind, falls ihr die HTML-Seiten lokal generieren wollt.

### Anpassungen der Base URL für eigene Server

Wenn ihr die HTML-Seiten auf eurem eigenen Server bereitstellen wollt, dann müsst ihr die Base URL eures Servers im Buildprozess anpassen. Die Base URL findet sich an folgenden Stellen:

- ```_assembly/scripts/make-html.sh```: BASE_URL=...
- ```_assembly/scripts/make-html.sh```: BASE_URL_ESCAPED=..., bitte alle slashes '/' ersetzen durch '\\\/'.

## Visual Studio Code Plugins

Die folgenden Plugins sind nützlich, um die Markdowndateien zu pflegen.

- [Prettier Code Formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Einheitliches Format für Markdown
- [Format Files](https://marketplace.visualstudio.com/items/?itemName=jbockle.jbockle-format-files): Erlaubt das Formatieren aller Dateien in einem Verzeichnis.
