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
'''

#Tri de tableaux
def trier(liste):
    liste_triee=[None]*len(liste)
    liste_triee[0]=liste[0]
    for index_liste in range(1,(len(liste)-1)):
        index_pge=0
        while liste_triee[index_liste]!=None:
            if liste[index_liste]>liste_triee[index_pge]:
                index_pge+=1
        for id2 in range(0,index_pge):
            liste_triee[index_liste-id2+1]=liste_triee[index_liste-id2]
        liste_triee[index_pge]=liste[index_liste]
    return liste_triee


print(trier([1,7,4,7,2,5,0,65]))



def killdoublons(liste):

    return liste


























