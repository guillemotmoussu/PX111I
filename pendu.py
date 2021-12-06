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
    element=pile[nombre_elements(pile)+1]
    pile-=pile[0]
    return pile,element
























print(nombre_elements(create_pile(5)))