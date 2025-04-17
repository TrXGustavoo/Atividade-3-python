from pato_borracha import PatoBorracha
from pato_bravo import PatoBravo
from pato_ruivo import PatoRuivo
from comportamentos_danca import Danca_Samba, Danca_Tango, NaoDanca

if __name__ == "__main__":
    pato1 = PatoBorracha()
    print(pato1.realizar_mostrar())
    print(pato1.realizar_nadar())
    print(pato1.realizar_voo())
    print(pato1.realizar_danca())

    print("------")

    pato2 = PatoBravo()
    print(pato2.realizar_mostrar())
    print(pato2.realizar_voo())
    print(pato2.realizar_grasnar())
    print(pato2.realizar_danca())
    print(pato2.realizar_pulo())
    
    print("------")
    
    pato3 = PatoRuivo()
    print(pato3.realizar_mostrar())
    print(pato3.realizar_voo())
    print(pato3.realizar_grasnar())
    print(pato3.realizar_danca())
    
    print("------")

    print("Mudando dança do Pato Bravo...")
    pato2.comportamento_dancar = Danca_Samba()
    print(pato2.realizar_danca())  
    
    print("------")
    
    print("Pato borracha aprende a dançar tango...")
    pato1.comportamento_dancar = Danca_Tango()
    print(pato1.realizar_danca()) 