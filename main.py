from pato_borracha import PatoBorracha
from pato_bravo import PatoBravo
from pato_ruivo import PatoRuivo
from comportamentos_danca import Danca_Samba, Danca_Tango, NaoDanca

if __name__ == "__main__":
    pato1 = PatoBorracha()
    print(pato1.mostrar())
    print(pato1.nadar())
    print(pato1.realizar_voo())
    print(pato1.realizar_danca())

    print("------")

    pato2 = PatoBravo()
    print(pato2.mostrar())
    print(pato2.realizar_voo())
    print(pato2.grasnar())
    print(pato2.realizar_danca())
    print(pato2.pular())
    
    print("------")
    
    pato3 = PatoRuivo()
    print(pato3.mostrar())
    print(pato3.realizar_voo())
    print(pato3.grasnar())
    print(pato3.realizar_danca())
    
    print("------")

    # print("Mudando dança do Pato Bravo...")
    # pato2.comportamento_dancar = Danca_Samba()
    # print(pato2.comportamento_dancar())
    
    # print("------")
    
    # print("Pato borracha aprende a dançar tango...")
    # pato2.comportamento_dancar = Danca_Samba()
    # print(pato2.comportamento_dancar())
