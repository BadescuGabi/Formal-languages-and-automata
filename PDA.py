def my_function(x):
  return x[::-1]

f = open("APD.txt","r")
cuvant = input()
copie=list(cuvant)
copie2=copie.copy()
for x in range(10):
    copie.append(" ")
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
Stiva=['Z']
VARIABILA = 0
ok_afis = 0
copie_stiv=['Z']
copie_dp = []  # folosim pentru a vedea daca am ajuns de mai mult de 2 ori in aceeasi situatie gen [0,1,2,0]
alfabet = [x for x in f.readline().split()]
st_init = int(f.readline())  # starea initiala
nr_stari_finale = f.readline()  # numarul de stari finale
lista_stari_finale = []  # lista cu ele
for x in f.readline().split():
    lista_stari_finale.append(int(x))
for x in cuvant:
    if x not in alfabet:
        print("nu este cuvant")
        exit()  # verifc daca cuvantul contine litere din alfabet
if cuvant=="&" and st_init in lista_stari_finale:
    print("este cuvant")
    exit()
lista_stari = []
for x in range(int(f.readline())):
    lista_stari.append([x])  # o lista ce contine starile de ex [0,1,2,3]
nr_tranzitii = int(f.readline())
for x in range(nr_tranzitii):
    lista_pentru_tuplu = []
    for y in f.readline().split():
        lista_pentru_tuplu.append(y)
    lista_pentru_tuplu[0] = int(lista_pentru_tuplu[0])
    lista_pentru_tuplu = tuple(lista_pentru_tuplu)
    lista_stari[lista_pentru_tuplu[0]].append(lista_pentru_tuplu)
# print(lista_stari) #prima cifra este data de starea in care se afla(q1,q2....) apoi tuple-urile reprezinta unde urmeaza sa se duca si cu ce litera
DP = [st_init]  # DP reprezinta unde ne aflam in momentul curent
indice_cuv = 0  # folosit ca indicele cuvantului
lista_vizita = []  # bagam aici toate muchile prin care am trecut
lista_vizite_moarte = []  # daca nu am gasit solutia, vom adauga aici muchiile care pleaca din acelasi nod si  care au aceeasi litera
while DP != []:
    y = lista_stari[DP[len(DP) - 1]]
    yy=copie_stiv[-1]
    Stiva=list(yy)
    ok = 0
    for x in y:
        if type(x) == tuple:
            ok2=0
            if indice_cuv==len(cuvant):
                if (str(x[2]) == str(copie[indice_cuv]) or (str(x[2])=="&")):
                    if (x not in lista_vizite_moarte):
                        if (str(x[3])==str(Stiva[len(Stiva)-1]) ):  # daca suntem pe muchia cu litera corespunzatoare si ea nu a mai fostvizitata
                           if str(x[3])!="Z":
                               for z in str(x[4]):
                                   if z=="Z" and str(x[2])!="Z":
                                       for z2 in Stiva:
                                           if z2=="Z":
                                               ok2=1
                           if ok2==0:
                                   ok = 1
                                    # if int(x[1]) != VARIABILA:
                                       #  lista_vizite_moarte = []
                                   print(Stiva)
                                   if(str(x[3])!="&"):
                                         Stiva.pop()
                                   if(str(x[4]))!="&":
                                       copie_str=str(" ".join(my_function(str(x[4]))).split(" ")).strip("[\]")
                                       for j in copie_str:
                                           if j>='A' and j<='Z':
                                                 Stiva.append(j)
                                   copie_stiv.append(Stiva.copy())
                                   DP.append(int(x[1]))
                                   print(DP)

                                   lista_vizita.append(x)
                                   if str(x[2])!="&":
                                        indice_cuv += 1
                                   if indice_cuv == len(cuvant) and DP[len(DP) - 1] in lista_stari_finale and (Stiva==[] or Stiva==["Z"]):  # cazul in care este cuvant  si e in stare finala
                                        print("este cuvant")
                                        exit()
                                   if indice_cuv == len(cuvant) and DP[len( DP) - 1] not in lista_stari_finale:  # cazul in care are lungimea cuvantului dar nu e o stare finala
                                        ok = 1
                                   break
            else:
                if (str(x[2]) == str(copie[indice_cuv]) or str(x[2]) == "&"):
                    if (x not in lista_vizite_moarte):
                        if (str(x[3]) == str(Stiva[len(
                                Stiva) - 1])):  # daca suntem pe muchia cu litera corespunzatoare si ea nu a mai fostvizitata
                            if str(x[3]) != "Z":
                                for z in str(x[4]):
                                    if z == "Z" and str(x[2]) != "Z":
                                        for z2 in Stiva:
                                            if z2 == "Z":
                                                ok2 = 1
                            if ok2 == 0:
                                ok = 1
                                # if int(x[1]) != VARIABILA:
                                #  lista_vizite_moarte = []
                                print(Stiva)
                                Stiva.pop()
                                if (str(x[4])) != "&":
                                    copie_str = str(" ".join(my_function(str(x[4]))).split(" ")).strip("[\]")
                                    for j in copie_str:
                                        if j >= 'A' and j <= 'Z':
                                            Stiva.append(j)
                                copie_stiv.append(Stiva.copy())
                                DP.append(int(x[1]))
                                print(DP)

                                lista_vizita.append(x)
                                if str(x[2]) != "&":
                                    indice_cuv += 1
                                if indice_cuv == len(cuvant) and DP[len(DP) - 1] in lista_stari_finale and (
                                        Stiva == [] or Stiva == [
                                    "Z"]):  # cazul in care este cuvant  si e in stare finala
                                    print("este cuvant")
                                    exit()
                                if indice_cuv == len(cuvant) and DP[len(
                                        DP) - 1] not in lista_stari_finale:  # cazul in care are lungimea cuvantului dar nu e o stare finala
                                    ok = 1
                                break
    if ok == 0:
        if(lista_vizita!=[]):
             lista_vizite_moarte.append(lista_vizita[len(lista_vizita) - 2])
        VARIABILA = DP[len(DP) - 1]
        copie_dp.append(DP)
        copie_stiv.pop()
        Stiva=copie_stiv
        if copie_dp.count(DP)>100:
            print("nu e cuvant")
            exit()
        DP.pop()
        indice_cuv -= 1
print("nu e cuvant")
#print(lista_vizita)
#print(lista_vizite_moarte)
#print(DP)

# imi intra in bucla pe unele cuvinte
#c este lambda

"""" 
input: 
a b c
0
3
1 3 0
5
13
0 1 a
0 1 b
0 4 a
1 0 b
1 2 a
1 4 b
2 1 b
2 3 b
3 2 a
3 4 c
4 1 b
4 2 a
4 2 b
4 3 a
"""