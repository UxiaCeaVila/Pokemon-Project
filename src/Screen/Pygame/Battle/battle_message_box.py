from Screen.Pygame.pygame_helper import GetTransparentSurface
from Screen.Pygame.MessageBox.message_box import MessageBox

from kao_gui.pygame.widgets.sized_widget import SizedWidget

class BattleMessageBox(SizedWidget):
    """ Represents the Message Box for a Battle """
    
    def __init__(self, battle, width, height):
        """ Initialize the Battle Message Box """
        SizedWidget.__init__(self, width, height)
        self.messageBox = MessageBox("")
        self.battle = battle
        
    def update(self):
        """ Update the screen """
        if not self.battle.noMessages() and not self.battle.messageQueue[0] == self.messageBox.message:
            self.messageBox = MessageBox(self.battle.messageQueue[0])
        self.messageBox.update()
        
    def drawSurface(self):
        """ Draw the child Message Box """
        surface = GetTransparentSurface(self.width, self.height)
        messageBoxSurface = self.messageBox.draw()
        self.drawOnSurface(messageBoxSurface, centerx=.5, centery=.5)