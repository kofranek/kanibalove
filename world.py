      #Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#R:/p1_PGM/p1_PYT/game_versions/game_v1a/world.py
"""
Modul world reprezentuje svět a obsahuje definice tříd prostorů,
předmětů (h-objektů) a člunu (batohu).
"""
from dbg import DBP #, DBG
DBP(0, f'===== Modul {__name__} ===== START')
############################################################################

############################################################################
class Item():
    """Instance reprezentují h-objekty v prostorech hry a ve člunu.
    V našem případě to budou tři kanibalové a tři misionáři"""

    def __init__(self, name: str):
        """Vytvoří h-objekt se zadaným názvem."""
        self.name = name


############################################################################
class Place:
    """Instance reprezentují prostory hry.
    V našem případě to bude Lev_břeh a Pravý_břeh"""

    def __init__(self, name: str):
        """Vytvoří prostor se zadaným názvem."""
        self.name = name


############################################################################
class Boat:
    """Instance třídy reprezentuje člun (batoh)."""

    CAPACITY = 2    # Maximální kapacita 2


############################################################################

# Aktuální prostor = prostor, v němž se hráč právě nachází
current_place = None

# Jediná instance člunu (batohu)
BOAT = Boat()


############################################################################
DBP(0, f'===== Modul {__name__} ===== STOP')
