# Dungeonslayers

[Dungeonslayers](https://dungeonslayers.net/) ist ein freies Pen & Paper Rollenspiel, entwickelt von **Christian Kennig**. Es ist lizensiert unter der Lizenz [CC BY-NC-SA 3.0 DE](https://creativecommons.org/licenses/by-nc-sa/3.0/de/deed.de). 

In diesem Repository sollen die unterschiedlichen Regeln aus dem Grundregelwerk, sowie aus unterschiedlichen Fanwerken gesammelt und in einheitlichem Format angeboten werden. Das Format ist Markdown.

Es handelt sich dabei um ein Fanprojekt. Die offizielle Dungeonslayers-Webpage ist unter dem Link [https://dungeonslayers.net/](https://dungeonslayers.net/) zu finden.

Die Markdown-Dateien bilden die Grundlage für das [DS4 SRD+](https://ronineighty.github.io/Dungeonslayers/).

## HTML-Seiten generieren

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
