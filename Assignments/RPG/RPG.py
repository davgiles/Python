#  File: RPG.py
#  Description: A simple text-based RPG game starring Harry Potter and Aragorn
#  Student's Name: David Giles
#  Student's UT EID: dgg524
#  Course Name: CS 313E 
#  Unique Number: 86940
#
#  Date Created: 06/09/17
#  Date Last Modified: 06/13/17


class Weapon:

    def __init__(self, type='none'):
        self.type = type
        self.damage = 0

        if self.type == 'dagger':
            self.damage = 4
        if self.type == 'axe':
            self.damage = 6
        if self.type == 'staff':
            self.damage = 6
        if self.type == 'sword':
            self.damage = 10

    def __str__(self):
        return(str(self.type))

class Armor:

    def __init__(self, type='none'):
        self.type = type
        self.ac = 10

        if self.type == 'plate':
            self.ac = 2
        if self.type == 'chain':
            self.ac = 5
        if self.type == 'leather':
            self.ac = 8

    def __str__(self):
        return(str(self.type))

class RPGCharacter:

    def __init__(self, name):
        self.name = name
        self.maxhp = 0
        self.hp = 0
        self.maxsp = 0
        self.sp = 0
        self.weapon = Weapon()
        self.armor = Armor()

    def wield(self, weapon):
        if self.type == 'wizard':
            if weapon.type == 'sword' or weapon.type == 'axe':
                print('Weapon not allowed for this character class.')
            else:
                self.weapon = weapon
        else:
            self.weapon = weapon

        print(self.name+' is now wielding a(n) '+str(self.weapon))

    def unwield(self):
        self.weapon = Weapon()
        print(self.name+' is no longer wielding anything.')

    def putOnArmor(self, armor):
        if self.type == 'wizard':
            print('Armor not allowed for this character class.')
        else:
            self.armor = armor

        print(self.name+' is now wearing '+str(self.armor))

    def takeOffArmor(self):
        self.armor = Armor()
        print(self.name+' is no longer wearing anything.')

    def fight(self, char):
        print(self.name+' attacks '+char.name+' with a(n) '+str(self.weapon))
        char.hp = char.hp - self.weapon.damage
        print(self.name+' does '+str(self.weapon.damage)+' damage to '+char.name+'!')
        print(char.name+' is now down to '+str(char.hp)+' health.')
        self.checkForDefeat(char)

    def checkForDefeat(self, char):
        if char.hp <= 0:
            print(char.name+' has been defeated!')
        return

    def show(self):
        print('\n  '+str(self.name))
        print('\tCurrent Health: '+str(self.hp))
        print('\tCurrent Spell Points: '+str(self.sp))
        print('\tWielding: '+str(self.weapon))
        print('\tWearing: '+str(self.armor))
        print('\tArmor Class: '+str(self.armor.ac)+'\n')
        
class Fighter(RPGCharacter):

    def __init__(self, name):
        RPGCharacter.__init__(self, name)
        self.type = 'fighter'
        self.maxhp = 40
        self.hp = 40
        self.maxsp = 0
        self.sp = 0

class Wizard(RPGCharacter):

    def __init__(self, name):
        RPGCharacter.__init__(self, name)
        self.type = 'wizard'
        self.maxhp = 16
        self.hp = 16
        self.maxsp = 20
        self.sp = 20

    def castSpell(self, spell, char):
        if spell == 'Fireball':
            cost = 3
            damage = 5
            if cost > self.sp:
                print('Insufficient spell points.')
                return
            else:
                print(self.name+' casts '+spell+' at '+char.name)
                char.hp -= damage
                self.sp -= cost
                print(self.name+' does '+str(damage)+' damage to '+char.name+'!')
                print(char.name+' is now down to '+str(char.hp)+' health.')
                self.checkForDefeat(char)
        elif spell == 'Lightning Bolt':
            cost = 10
            damage = 10
            if cost > self.sp:
                print('Insufficient spell points.')
                return
            else:
                print(self.name+' casts '+spell+' at '+char.name)
                char.hp -= damage
                self.sp -= cost
                print(self.name+' does '+str(damage)+' damage to '+char.name+'!')
                print(char.name+' is now down to '+str(char.hp)+' health.')
                self.checkForDefeat(char)
        elif spell == 'Heal':
            cost = 6
            damage = -6
            if cost > self.sp:
                print('Insufficient spell points.')
                return
            else:
                print(self.name+' casts '+spell+' at '+char.name)
                char.hp -= damage
                self.sp -= cost
                if char.hp > char.maxhp:
                    char.hp = char.maxhp
                print(self.name+' heals '+char.name+' for 6 health points!')
                print(char.name+' is now up to '+str(char.hp)+' health.')
                self.checkForDefeat(char)
        else:
            print('Unknown spell name. Spell failed.')
            return
    
    
def main():

    chainMail = Armor('chain')
    sword = Weapon('sword')
    staff = Weapon('staff')
    axe = Weapon('axe')

    harry = Wizard('Harry Potter')
    harry.wield(staff)
    
    aragorn = Fighter('Aragorn')
    aragorn.putOnArmor(chainMail)
    aragorn.wield(axe)
    
    harry.show()
    aragorn.show()

    harry.castSpell('Fireball',aragorn)
    aragorn.fight(harry)

    harry.show()
    aragorn.show()

    harry.castSpell('Lightning Bolt',aragorn)
    aragorn.wield(sword)

    harry.show()
    aragorn.show()

    harry.castSpell('Heal',harry)
    aragorn.fight(harry)

    harry.fight(aragorn)
    aragorn.fight(harry)

    harry.show()
    aragorn.show()

main()
