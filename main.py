from checker import handleInputInteger
from logicNiederlassung import getNiederlassung
from logicMitarbeiter import getMitarbeiter
from logicAuftrag import getAuftrag, anlegenAuftrag, planenAuftrag, erledigenAuftrag
from logicErsatzteil import getErsatzteilListe, getErsatzteilForAuftrag

# Aufruf der Ablauflogik
while True:
    print('')
    print('1 - Daten anzeigen')
    print('2 - Neuen Auftrag anlegen')
    print('3 - Auftrag planen')
    print('4 - Auftrag erledigen')
    print('5 - Ersatzteile anzeigen')
    wastun = handleInputInteger('Aktion wählen')
    print()

    if wastun == 1:
        nlnr = getNiederlassung()  # Niederlassung aus Niederlassungsliste auswählen
        while nlnr > 0:
            print()
            mitnr = (nlnr)  # Mitarbeiter aus Mitarbeiterliste auswählen
            while mitnr > 0:
                print()
                aufnr = getAuftrag(mitnr)  # Aufträge des Mitarbeiters anzeigen
                while aufnr > 0:
                    #getErsatzteilForAuftrag(aufnr) # zu ergänzen - Ersatzteile des Auftrags anzeigen
                    aufnr = getAuftrag(mitnr)  # neue Aufträge des Mitarbeiters anzeigen
                mitnr = getMitarbeiter(nlnr)  # neuen Mitarbeiter aus Mitarbeiterliste auswählen
            nlnr = getNiederlassung()  # neue Niederlassung aus Niederlassungsliste auswählen
    elif wastun == 2:
        print('Daten einfügen')
        anlegenAuftrag()
    elif wastun == 3:
        print('Auftrag planen')
        planenAuftrag()
    elif wastun == 4:
        print('Auftrag erledigen')
        erledigenAuftrag()
    elif wastun == 5:
        print('Anzeige der Ersatzteilliste')
        getErsatzteilListe()
    else:
        break