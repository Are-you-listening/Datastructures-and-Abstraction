"""ADT Reservatie_Systeem"""

import Film,Gebruiker,Reservatie,Vertoning,Zaal,MyQueue_Linked,MyBST,MyTwoThreeFourTree,MyCircularLinkedChain

"""Implementatie via een Queue"""
class Reservatiesysteem:
    def __init__(self):
        #Data
        """
        Construeert een Reservatiesysteem object
        :parameter in ;
        :parameter out ; 'reservaties': MyQueue , 'users': MyQueue , 'films': MyQueue , 'zalen': MyQueue , 'vertoningen', My234T , 'tijdslots': Python-List met integers, 'timestamp': int (intialized on 0), 'idcounter': int (0)
        Preconditie:
        Postconditie: Een reservatiesysteem is geconstrueerd met de paramaters.
        """
        self.reservaties=MyQueue_Linked.MyQueue() #Reservaties bijhouden
        self.users=MyCircularLinkedChain.MyLinkedChain()
        self.films=MyCircularLinkedChain.MyLinkedChain()
        self.zalen=MyCircularLinkedChain.MyLinkedChain()
        self.vertoningen=MyTwoThreeFourTree.TwoThreeFourTree()
        self.tijdslots=[14*3600+30*60,17*3600,20*3600,22*3600+30*60] #In seconden 14u30,17:00,20:00,22:30
        self.timestamp=0 #Tijd
        self.idcounter=0 #Verhoogt per ID in de trees

    def add_reservation(self,Reservatie):
        """
        Methode om Reservaties toe te voegen
        :parameter in ; 'Reservatie': Reservatie-Object
        :parameter out ; bool: 'Succes' (#succes = self.reservaties.enqueue(Reservatie)
        Preconditie: Reservatie != None
        Postconditie: Bij 'Succes' is de 'Reservatie' toegevoegd aan de Queue "self.reservaties"
        """
        Reservatie.id=self.idcounter #Set ID
        self.idcounter+=1
        #if(succes==True):
        print(Reservatie.id , "toegevoegd aan de chain")

    def add_gebruiker(self,user):
        """
        Methode om Gebruikers toe te voegen
        :parameter in ; 'user': Gebruiker-Object
        :parameter out ; bool: 'Succes'  #succes = self.users.insert(lengte,Gebruiker)
        Preconditie: 'user' heeft nog geen ID toegewezen. user != None
        Postconditie: Bij 'Succes' is de 'user' toegevoegd aan de Queue "self.users"
        """
        lengte = self.users.getLength()+1 #Vraag lengte v/d lijst op
        user.id=lengte #Set ID
        print(user.email, "toegevoegd aan de chain")

    def add_film(self,movie):
        """
        Methode om Films toe te voegen
        :parameter in ; 'movie': Film-Object
        :parameter out ; bool: 'Succes' #succes = self.film.insert(lengte,Gebruiker)
        Preconditie: 'movie' heeft nog geen ID toegewezen. , movie != None
        Postconditie: Bij 'Succes' is de 'movie' toegevoegd aan de Queue "self.films"
        """
        lengte = self.users.getLength()+1 #Vraag lengte v/d lijst op
        movie.id=lengte #Set ID
        print(movie.titel, "toegevoegd aan de chain")

    def add_zaal(self,zaal):
        """
        Methode om zalen toe te voegen
        :parameter in ; 'zaal': Zaal-Object
        :parameter out ; bool: 'Succes'         #succes = self.zalen.insert(lengte,Gebruiker)
        Preconditie: 'zaal' heeft nog geen ID toegewezen. zaal != None
        Postconditie: Bij 'Succes' is de 'zaal' toegevoegd aan de Queue "self.zalen"
        """
        lengte = self.zalen.getLength()+1 #Vraag lengte v/d lijst op
        zaal.id=lengte #Set ID
        print(zaal.nummer, "toegevoegd aan de chain")

    def add_vertoning(self,vertoning):
        """
        Methode om vertoningen toe te voegen
        :parameter in ; 'vertoning': vertoningObject
        :parameter out ; bool: 'Succes'
        Preconditie: 'vertoning' heeft nog geen ID toegewezen. vertoning != None
        Postconditie: Bij 'Succes' is 'vertoning' toegevoegd aan de Queue "self.vertoningen"
        """
        vertoning.id=self.idcounter
        self.idcounter+=1
        print(vertoning.id, "toegevoegd aan de chain")

    def setTime(self,timestamp):
        """
        Past de 'currenttimestamp' aan op 'timestamp'
        :parameter in ; 'timestamp': int
        :parameter out ;
        Preconditie:
        Postconditie: Timestamp is aangepast.
        """
        self.timestamp=timestamp
        print("Tijd is aangepast op timestamp: " , timestamp)

    def inc_time(self):
        """
        Verhoogt de 'currenttimestamp' met 1 maar blijft binnen de uren.
        :parameter in ;
        :parameter out ;
        Preconditie:
        Postconditie: Timestamp is aangepast.
        """
        if(self.timestamp==3):
            self.timestamp=0
            return
        self.timestamp+=1
        print("De tijd is verhoogd")

    def reservation_out(self):
        """
        Leest een reservatie uit.
        :parameter in ;
        :parameter out ;
        Preconditie:
        Postconditie: reservations is gedequeed
        """
        reservatie = prototype.reservaties.getFront()
        print("Reservatie is uitgelezen")         #reservatie.print()
        #aantal_plaatsen=reservatie.aantal_plaatsen
        #vertoning=self.vertoningen.retrieveItem(reservatie.vertoningid)
        #if(vertoning.vrije_plaatsen>(vertoning.ingenomen_plaatsen+aantal_plaatsen)):
        #    vertoning.ingenomen_plaatsen+=aantal_plaatsen #Verlaag het aantal plaatsen
        #    print("Het aantal vrije plaatsen is verlaagd")
        print("Het aantal vrije plaatsen is verlaagd")
        #else:
            #print("Error: Zaal vol")
        prototype.reservaties.dequeue()
        print("De reservatie is verwijdert")
        self.inc_time()#Verhoog tijd, LET OP: mag niet buiten de uren gaan

    def start_vertoning(self,vertoning):
        """
        Start een vertoning.
        :parameter in ; 'vertoning': Vertoning
        :parameter out ; 'succes': bool
        Preconditie: De vertoning is nog niet gestart.
        Postconditie: De vertoning start indien alle reservaties zijn gevalideerd
        """
        #Valideer reservaties
        print(vertoning.id, "is gestart")
        self.inc_time()

    def stop_vertoning(self,vertoning):
        """
        Stop een vertoning.
        :parameter in ; 'vertoning': Vertoning
        :parameter out ; 'succes': bool
        Preconditie: De vertoning is gestart
        Postconditie: De vertoning stopt
        """
        vertoning.ingenomen_plaatsen=0
        #Indien juiste stamps
        #Moeten we bijhouden of een vertoning bezig is ja/nee?

    def delete_vertoningen(self):
        """
        Cleart self.vertoningen
        :parameter in ;
        :parameter out ;
        Preconditie:
        Postconditie:
        """
        #Moet er iets gesaved worden//output?
        #delete all items or set op =None
        self.vertoningen=MyTwoThreeFourTree.TwoThreeFourTree()
        print("Alle vertoningen verwijdert")
        return True

    def delete_films(self):
        """
        Cleart self.films
        :parameter in ;
        :parameter out ;
        Preconditie:
        Postconditie:
        """
        #Moet er iets gesaved worden//output?
        #delete all items or set op =None
        self.films=MyCircularLinkedChain.MyLinkedChain()
        print("Alle films verwijdert")
        return True

    def delete_gebruikers(self):
        """
        Cleart self.users
        :parameter in ;
        :parameter out ;
        Preconditie:
        Postconditie:
        """
        #Moet er iets gesaved worden//output?
        #delete all items or set op =None
        self.users=MyCircularLinkedChain.MyLinkedChain()
        print("Alle users verwijdert")
        return True

#TO DO:
#Circulair Chain aanpassen (constructor juist aanroepen -> anders ID gone)
#Films linken aan Vertoningen?
#Hard idea: 1 add command maken?
vertoningen = [0,1,2,3] # 0 = 14:30 , 1=17:00 , 2=20:00 , 3=22:30

prototype = Reservatiesysteem()
Tom = Gebruiker.Gebruiker("Tom","Hofkens","Tom@mail")
prototype.add_gebruiker(Tom)
Els = Gebruiker.Gebruiker("Els","Laenens","Els@mail")
prototype.add_gebruiker(Els)
TheMatrix = Film.Film("TheMatrix",9)
prototype.add_film(TheMatrix)
Zaal1 = Zaal.Zaal(1,45)
prototype.add_zaal(Zaal1)
Vertoning_TheMatrix = Vertoning.Vertoning(Zaal1.nummer,2,None,TheMatrix.id,Zaal1.aantal_plaatsen)
prototype.add_vertoning(Vertoning_TheMatrix)
Interception = Film.Film("InterCeption",0)
prototype.add_film(Interception)
Vertoning_Interception = Vertoning.Vertoning(Zaal1.nummer,0,None,Interception.id,Zaal1.aantal_plaatsen)
prototype.add_vertoning(Vertoning_Interception)
Reservatie_Tom = Reservatie.Reservatie(Tom.id,0,Vertoning_Interception.id,5)
prototype.add_reservation(Reservatie_Tom)
Reservatie_Els = Reservatie.Reservatie(Els.id,1,Vertoning_Interception.id,2)
prototype.add_reservation(Reservatie_Els)
prototype.setTime(2)
prototype.reservation_out() #1e reservatie
prototype.reservation_out() #2e reservatie
prototype.start_vertoning(Vertoning_Interception)
prototype.stop_vertoning(Vertoning_Interception)
prototype.start_vertoning(Vertoning_TheMatrix)
prototype.stop_vertoning(Vertoning_TheMatrix)
#Wanneer het reservatiesysteem out of scope gaat wordt alles verwijdert? -> Er is een handmatige optie nodig?
prototype.delete_vertoningen()
prototype.delete_films()
prototype.delete_gebruikers()