# from Screen.Console.screen import Screen
# from logo import Logo
# from menu_view import MenuView

from kao_gui.console.console_widget import ConsoleWidget

class MainMenuScreen(ConsoleWidget):
    """ Represents the Main Menu screen """
    
    def __init__(self, menu):
        """  """
        self.menu = menu
        # self.logo = Logo()
        # self.menuView = MenuView(menu)
        
    def draw(self):
        """ Draws the screen to the provided window """
        print "Welcome to the Pokemon Console Version"
        # self.drawLogo(window)
        # self.drawMenu(window)
        
    def drawLogo(self, window):
        """ Draws the Logo to the window """
        logoText, logoSize = self.logo.draw(window)
        logoPos = self.getCenteredRect(window, logoSize, .5, .25) 
        window.draw(logoText, logoPos)
        
    def drawMenu(self, window):
        """ Draws the Menu to the window """
        menuText, menuSize= self.menuView.draw(window)
        menuPos = self.getCenteredRect(window, menuSize, .5, 11.0/16) 
        window.draw(menuText, menuPos)
        