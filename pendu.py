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
    for index in range(1,(len(liste)-1)):
        indecse=0
        while indecse<index-1 and liste[index]<liste_triee[indecse]:
            indecse+=1
        for id2 in range(indecse,index):
            liste_triee[index-id2+1]=liste_triee[index-id2]
        liste_triee[indecse]=liste[index]
    return liste_triee


print(trier([1,7,4,7,2,5,0,65]))



def killdoublons(liste):

    return liste


























