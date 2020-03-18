f=open("automat.txt")
cuvant=input()
"""
 -->alfabet
0 ---> stare initiala
1 ---> numar de stari finale
3 ---> starea finala
4 --->nr de stari
8 --->numar de tranzitii
0 1 a
0 0 b
1 1 a
1 2 b
2 0 b
2 3 a
3 3 a
3 3 b
"""
VARIABILA=0
alfabet=[x for x in f.readline().split()]
for x in cuvant:
    if x not in alfabet:
        print("nu este cuvant")
        exit() #verifc daca cuvantul contine litere din alfabet
st_init=int(f.readline()) #starea initiala
nr_stari_finale=f.readline() #numarul de stari finale
lista_stari_finale=[] #lista cu ele
for x in f.readline().split():
    lista_stari_finale.append(int(x))
lista_stari=[]
for x in range(int(f.readline())):
        lista_stari.append([x]) #o lista ce contine starile de ex [0,1,2,3]
nr_tranzitii=int(f.readline())
for x in range(nr_tranzitii):
    lista_pentru_tuplu=[]
    for y in f.readline().split():
        lista_pentru_tuplu.append(y)
    lista_pentru_tuplu[0]=int(lista_pentru_tuplu[0])
    lista_pentru_tuplu=tuple(lista_pentru_tuplu)
    lista_stari[lista_pentru_tuplu[0]].append(lista_pentru_tuplu)
print(lista_stari) #prima cifra este data de starea in care se afla(q1,q2....) apoi tuple-urile reprezinta unde urmeaza sa se duca si cu ce litera
DP=[st_init] #DP reprezinta unde ne aflam in momentul curent
indice_cuv=0 #folosit ca indicele cuvantului
lista_vizita=[] #bagam aici toate muchile prin care am trecut
lista_vizite_moarte=[] #daca nu am gasit solutia, vom adauga aici muchiile care pleaca din acelasi nod si  care au aceeasi litera
while DP!=[]:
    y=lista_stari[DP[len(DP)-1]]
    ok=0
    for x in y:
        if type(x)==tuple:
            if str(x[2])==str(cuvant[indice_cuv]) and x not in lista_vizite_moarte : #daca suntem pe muchia cu litera corespunzatoare si ea nu a mai fostvizitata
                ok=1
                if int(x[1])!=VARIABILA:
                    lista_vizite_moarte=[]
                DP.append(int(x[1]))
                print(DP)
                lista_vizita.append(x)
                indice_cuv+=1
                if indice_cuv==len(cuvant) and DP[len(DP)-1]  in lista_stari_finale: #cazul in care este cuvant  si e in stare finala
                     print("este cuvant")
                     exit()
                if indice_cuv==len(cuvant) and DP[len(DP)-1] not in lista_stari_finale: #cazul in care are lungimea cuvantului dar nu e o stare finala
                    print("nu este cuvant")
                    exit()
                break
    if ok==0:
        lista_vizite_moarte.append(lista_vizita[len(lista_vizita)-2])
        VARIABILA=DP[len(DP)-1]
        DP.pop()
        indice_cuv-=1
print("nu e cuvant")
print(lista_vizita)
print(lista_vizite_moarte)
print(DP)
#imi intra in bucla pe unele cuvinte
