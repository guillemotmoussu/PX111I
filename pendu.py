def create_pile(capa):
    pile=(capa+1)*[None]
    pile[0]=0
    return pile



def nombre_elements(pile):
    nombre_elements_pile=pile[0]
    return nombre_elements_pile



#def empiler(element,pile):
    





def depiler(pile):
    element=pile[0]
    pile-=pile[0]
    return pile,element
























print(nombre_elements(create_pile(5)))