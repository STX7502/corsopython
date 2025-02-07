# Date 2 variabili a e b, invertine il valore delle due variabili
# il codice deve funzionare inpostando  qualunque valore di a e b




#a = 40
#b = 20

# soluzione 

#c = a
#a = b
#b = c

#print(a) 
#print(b)



# Scrivere un programma chiamato numerator
# Il programma deve:
# - Scrivere un messaggio di benvenuto al lancio, indicando il suo nome
# - Chiedere all'utente quattro numeri 
# - Sommare i numeri e stamparli a video
# - Chiedere un quinto numero
# - Sottrarlo dalla somma precedente e stamparlo a video

# Usare se necessario delle stampe per spiegare i valori che vengono mostrati all'utente


nome_programma = "Benvenuto nel Numeretor"
print(nome_programma)
primo_numero = input("inserire il primo numero:\n")

a = int(primo_numero)
print("hai inserito il valore:",a)

secondo_numero = input("inserisci il secondo numero:\n")
b = int(secondo_numero)
terzo_numero = input("inserire il terzo numero:\n")
c = int(terzo_numero)
quarto_nemero = input("inserire il quarto numero:\n")
d = int(quarto_nemero)

#print(type(primo_numero))






somma = a + b + c + d


print("Tot",somma)
totale_somma = somma
quinto_nemero = input("inserisci un ulteriore numero:\n")
e = int(quinto_nemero)
sottrazione = totale_somma - e
print("risultato ottenuto",sottrazione)




#primo_numero = int(input("inserisci il primo numero:\n"))







                     
