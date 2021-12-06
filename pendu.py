#Piles à capacité finie
def create_pile(capa):
    pile=(capa+1)*[None]
    pile[0]=0
    return pile

def nombre_elements(pile):
    return pile[0]

def empiler(element,pile):
    pile[pile[0]+1]=element
    pile[0]+=1
    return pile

def depiler(pile):
    element=pile[pile[0]]
    pile[0]-=1
    return pile,element

'''
pile=create_pile(5)
print(nombre_elements(pile))
pile=empiler("j",pile)
print(nombre_elements(pile))
pile,element=depiler(pile)
print(element)


#Tri de tableaux

def trier(liste):
    liste_triee=[]
    liste_triee+=[liste[0]]
    for index in range(1,(len(liste))):
        endroit_a_inserer=0
        for index2 in range(len(liste_triee)):
            if liste[index]>liste_triee[index2]:
                endroit_a_inserer=(index2+1)
        liste_triee=(liste_triee[:endroit_a_inserer]+[liste[index]]+liste_triee[endroit_a_inserer:])
    return liste_triee
print(trier([1,7,4,0,0,7,2,55,5,0,65]))

'''


def partie():
    mot=str(input("Quel est le mot : "))
    print ('\n' * 12)
    chances=8
    mot_a_trouver=("*"*len(mot))
    afficher_partie(mot_a_trouver,chances)

def afficher_partie(mot_a_trouver,chances):
    print(mot_a_trouver)
    print(chances)

partie()