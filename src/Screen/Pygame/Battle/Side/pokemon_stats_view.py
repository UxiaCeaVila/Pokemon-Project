from Menu.text_menu_entry import TextMenuEntry
from Menu.ActionMenu.SwitchMenu.pokemon_menu_entry import PokemonMenuEntry

from Screen.Pygame.pygame_helper import GetTransparentSurface
from Screen.Pygame.HealthBar.health_bar_view import HealthBarView
from Screen.Pygame.Menu.MainMenu.menu_entry_view import MenuEntryView

from kao_gui.pygame.pygame_widget import PygameWidget

class PokemonStatsView(PygameWidget):
    """ View for a Pokemon's Stats in a Battle """
    FONT_SIZE = 24
    
    def __init__(self, pokemon=None, pokemonMenuEntry=None, showHP=True):
        """ Initialize the Pokemon Stats View """
        if pokemon is not None:
            self.pokemon = pokemon
        else:
            self.pokemon = pokemonMenuEntry.getPokemon()
            
        self.showHP = showHP
        self.setPokemonMenuEntryView(pokemonMenuEntry)
        self.healthBarView = HealthBarView(self.pokemon)
        
    def setSize(self, width, height):
        """ Set the size of the widget """
        self.__height = height
        self.__width = width
        
        self.healthBarView.setSize(self.__width, self.__height*.1)
        
    def buildSurface(self):
        """ Return the surface for the widget """
        return GetTransparentSurface(self.__width, self.__height)
    
    def setPokemonMenuEntryView(self, pokemonMenuEntry):
        """ Sets the Pokemon Menu Entry """
        if pokemonMenuEntry is None:
            pokemonMenuEntry = PokemonMenuEntry(self.pokemon, None)
        self.pkmnEntryView = MenuEntryView(pokemonMenuEntry, self.FONT_SIZE)
        self.setLevelMenuEntryView()
        self.setHealthMenuEntryView()
        
    def setLevelMenuEntryView(self):
        """ Set the Level Menu Entry view """
        menuEntry = TextMenuEntry("Lv. {0}".format(self.pokemon.getLevel()), None)
        self.levelEntryView = MenuEntryView(menuEntry, self.FONT_SIZE)
        
    def setHealthMenuEntryView(self):
        """ Set the Level Menu Entry view """
        menuEntry = TextMenuEntry("{0}/{1}".format(self.pokemon.getCurrHP(), self.pokemon.getStat("HP")), None)
        self.healthEntryView = MenuEntryView(menuEntry, self.FONT_SIZE)
        
    def drawSurface(self):
        """ Draw the Pokemon Stats View """
        pkmnSurface = self.pkmnEntryView.draw()
        self.drawOnSurface(pkmnSurface, left=0, top=0)
        
        levelSurface = self.levelEntryView.draw()
        self.drawOnSurface(levelSurface, right=1, top=0)
        
        healthBarSurface = self.healthBarView.draw()
        self.drawOnSurface(healthBarSurface, left=0, top=(pkmnSurface.get_height()+10.0)/self.height)
        
        if self.showHP:
            healthSurface = self.healthEntryView.draw()
            self.drawOnSurface(healthSurface, right=1, 
                    top=(pkmnSurface.get_height()+healthBarSurface.get_height()+15.0)/self.height)
        
    def update(self):
        """ Update the Pokemon Stats View """
        self.setLevelMenuEntryView()
        self.setHealthMenuEntryView()