#!/usr/bin/env python3

print("kalukaèkčka\n")
pokracovat = True
while pokracovat:
      prvni_cislo = int(input("zadejte první číslo: "))
      druhe_cislo = int(input("zadejte druhe cislo: "))
      print("1 - sčítání")
      print("2 - odčítání")      
      print("3 - násobení")
      print("4 - dělení")
      cislo_operace = int(input("Zadejte číslo operace: "))
      if cislo_operace == 1:
            print("jejich součet je:", prvni_cislo + druhe_cislo)
      elif cislo_operace == 2:
          print("jejich rozdil jhe:", prvni_cislo - druhe_cislo)
      elif cislo_operace == 3:
            print("jejich soucit je:", prvni_cislo * druhe_cislo)
      elif cislo_operace == 4:
          print("jejich podíl je:", prvni_cislo / druhe_cislo)
      else:
          print("neplatna volba!")
      nezadano = True
      while nezadano:
            odpoved = input("\nPøejete si zadat dalsi priklad? y / n: ")
            if (odpoved == "y" or odpoved == "Y"):
                  nezadano = False
            elif (odpoved == "n" or odpoved == "N"):
                  nezadano = False
                  pokracovat = False
            else:
                  pass      
input("\nStiksnete libovlnou klávesu...")
