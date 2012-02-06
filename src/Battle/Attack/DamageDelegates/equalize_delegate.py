from Battle.Attack.DamageDelegates.damage_delegate import DamageDelegate

class EqualizeDelegate(DamageDelegate):
    """ Deals damage based on level """
    def __init__(self, parent, damage, physical):
        """ Set physical """
        self.parent = parent
        self.fixedDamage = damage
        self.physical = physical
        
    def damage(self, user, target):
        """ Returns  the damage of the attack
        including effectiveness and STAB """
        #user = actingSide.currPokemon
        #target = otherSide.currPokemon
        messages = []
        
        # Get damage
        damage = self.calcDamage(user, target)
        
        # Get modifiers
        mod = self.getEffectiveness(messages, target)
        mod = mod*self.getStab(user)
        mod = mod*self.getCrit(messages, user)
        
        return self.normalize(damage*mod), messages