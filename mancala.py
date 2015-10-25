def mancala():
# četrnaest prirodnih brojeva odvojenih razmakom koji predstavljaju broj kamenčića
# u svakom od 14 udubljenja u poretku 1-2-3-4-5-6-A-7-8-9-10-11-12-B.   
 ploca = [ 4, 4, 4, 4, 4, 4, 0, 4, 4, 4,  4,  4,  4,  0]
 potez = []
 saka = 0
 polje = 0
 broj_poteza = int(input("upisi_broj_poteza : "))
 for x in range(broj_poteza):
     x = int(input("potez " ))
     potez.append(x)
     if (x == 6) or (x ==13):
         potez.remove(x)
 print ("ispis prihvacenih poteza i njihovih promjena u indeks ploce") 
 def igraB(potez,ploca):
# eliminacija praznih poteza, poteza nad praznim poljima ploce i nedopustenih poteza
     if (ploca[potez[0]] == 0):
         potez.remove(potez[0])
         if (len(potez)>0):
             igraB(potez,ploca)
     elif not (7 <= potez[0] <= 12):
         potez.remove(potez[0])
         if (len(potez)>0):
             igraB(potez,ploca)        
     else:        
         saka = ploca[potez[0]]
         ploca[potez[0]] = 0
         polje = potez[0]
         potez.remove(potez[0])
         print(polje)
#sijanje kamenja po poljima preskacuci nedopustena i nepostojeca polja        
         while (saka !=0):
             polje = polje + 1
# Igračeva banka je uključena u obilazak dok se protivnikova banka preskače             
             if (polje == 14):
                 polje = 0
             if (polje == 6):
                 polje = 7
             ploca[polje] = ploca[polje] + 1
             saka = saka - 1
         if (polje == 13):
             if (len(potez)>0):
                 igraB(potez,ploca)
         else:
# Ako zadnji kamenčić završi u do tada praznom udubljenju na strani igrača na potezu
# i nasuprotno udubljenje na protivnikovoj strani bude neprazno,
#tada taj igrač u svoju banku preseljava kamenčiće iz oba udubljenja.

             if (7 <= polje <=12) and (ploca[polje] == 1) and (ploca[polje - 7] > 0):
                 ploca[13] = ploca[13] + ploca[polje - 7] + 1
                 ploca[polje - 7] = 0
                 ploca[polje] = 0
             if (len(potez)>0):
                 return igraA(potez,ploca)    
                 
 def igraA(potez,ploca):
# eliminacija praznih poteza, poteza nad praznim poljima ploce i nedopustenih poteza
     if (ploca[potez[0]] == 0):
         potez.remove(potez[0])
         if (len(potez)>0):
             igraA(potez,ploca)
     elif not (0 < potez[0] <= 6):
         potez.remove(potez[0])
         if (len(potez)>0):
             igraA(potez,ploca)        
     else:
#ovdje oduzimamo vrijednost broja polja jer je u izlazu zadatka naglašeno
#da lista(unos) pocinje od 1, a ne od 0, to se vidi iu stogo vece uvjetu povise
#U B podrucju to nismo trebali uciniti jer je lista refundirana bankom A         
         saka = ploca[potez[0]-1]
         ploca[potez[0]-1] = 0
         polje = potez[0]-1
         potez.remove(potez[0])
         print(polje)
#sijanje kamenja po poljima slicno kao u slucaju B       
         while (saka !=0):
             polje = polje + 1
             if (polje == 13):
                 polje = 0
             ploca[polje] = ploca[polje] + 1
             saka = saka - 1
         if (polje == 6):
             if (len(potez)>0):
                 igraA(potez,ploca)
         else:
             if (0 <= polje <=5) and (ploca[polje] == 1) and (ploca[polje + 7] > 0):
                 ploca[6] = ploca[6] + ploca[polje + 7] + 1
                 ploca[polje + 7] = 0
                 ploca[polje] = 0
             if (len(potez)>0):                 
                    return igraB(potez,ploca)    

 if (len(potez)>0):     
     igraB(potez,ploca)

 print(ploca)
mancala()



