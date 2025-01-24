from dbConnect import sessionLoader
from mapper import Ersatzteil
from mapper import Auftrag
from mapper import Montage

def getErsatzteilListe() :
    """ Definition der Funktion getErsatzteilListe().
    Diese Funktion ist im Rahmen des Praktikums zu implementieren.
    """
    session = sessionLoader()
    menge_et = session.query(Ersatzteil).all()

    # Wenn mehr als 0 Ersatzteile ermittelt werden konnten
    if len(menge_et)>0:
        # Defintion und Initialisierung der Liste der Niederlassungsnummern, 1. Element 0
        for et in menge_et:
            print(f' {et.EtID}  -  {et.EtBezeichnung} - {et.EtPreis} - {et.EtAnzLager} - {et.EtHersteller}')     # Ausgabe der Daten
        print()        
    
    else:
        print('Kein Ersatzteil in der DB.')
    session.close()
    
def getErsatzteilForAuftrag(p_aufnr, validAufNr) :
    """ Definition der Funktion getErsatzteilForAuftrag().
    Diese Funktion ist im Rahmen des Praktikums zu implementieren.
    
    :param p_aufnr - Auftragsnummer
    
    """

    if p_aufnr == 0:
        print()
        return
    
    session = sessionLoader()

    # check AufNr
    if p_aufnr not in validAufNr:
        print("Du hast keine gültige Auftragsnummer eingegeben.")
        print()
        return

    # execute
    #ersatzteile = session.query(Auftrag).filter(Auftrag.AufNr == p_aufnr).join(Montage).join(Ersatzteil).all()
    ersatzteile = session.query(Ersatzteil).join(Montage).join(Auftrag).filter(Auftrag.AufNr == p_aufnr).all()

    print()
    print("Alle verbauten Ersatzteile: ")
    if len(ersatzteile) > 0:
        for et in ersatzteile:
            # um Anzahl zu bekommen
            montage = session.query(Montage).filter(Montage.EtID == et.EtID).join(Auftrag).filter(Auftrag.AufNr == p_aufnr).first()
            print(f'{et.EtID} - {et.EtBezeichnung} - {montage.Anzahl}')
    else:
        print("Es wurden keine Ersatzteile bei diesem Auftrag verbaut")
    print()
    
    session.close()
