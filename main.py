# C'est ici le point de départ de notre petite application Python !

print('''Hello Word !
Truc à la con
Quel est ton âge ?''')

# Ici, je scan l'age de l'utilisateur. Ca va nous servir plus tard !
age = -1

while age < 0 :
    try:
        age = int(input('Sinon tu risques de ne pas pouvoir boire de la bière : \n'))
    except ValueError:
        print("Eh oh ! Tu ne me prendrais pas pour une andouille ?")

print ('Vous avez', age, 'ans.')

# On vérifie que l'utilisateur à au moins 18 ans
if age>17 : 
    print('Spèce dalcoolo !') 
else :
    print('Tu es trop jeune')
