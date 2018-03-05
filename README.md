# sentiment
## sentiment analysis project

### Wichtige Hinweise für die Abgaben
Jede Gruppe muss Ihre Systeme mit dem Test-Set selber auswerten, 
und den F-Score (siehe Bild unten) in der Abgabe-Email mir schicken.
Dieses F-Score ist, so zu sagen, die Performance unserer Systeme.

Für genauere Info, wie der Scorrer funktioniert, liest bitte die README_SCORER.txt Datei, den Teil Task B.

### Nachricht Polarity Klassifizierung
Die Aufgabe besteht darin, angesichts einer Tweet-Nachricht, zu klassifizieren, ob die Nachricht eine positive, negative oder neutrale Stimmung hat. Für die Nachrichten, die sowohl eine positive als auch eine negative Stimmung haben können, sollte die stärkere Stimmung gewählt werden.

### Format der Datensätze.
Die Daten, die zeilenweise in den Datensätzen gespeichert sind, haben den folgenden Format:

`ID1[TAB]ID2[TAB]Stimmung[TAB]Tweet-Nachricht`

`Bsp.: 111353863327596544	56547576	positive	Jersey shore season four tonight :) x`
