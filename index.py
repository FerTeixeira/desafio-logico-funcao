def calculateRank(win, loser):
    points = win - loser
    return points

while True:
    winPoints = int(input("Quantas partidas você ganhou: "))
    loserPoints = int(input("Quantas partidas você perder: "))
    rank = calculateRank(winPoints, loserPoints)

    if rank < 0:
        rank = 0

    if rank <= 10:
        ratings = "Ferro"
    
    elif rank >= 11 and  rank <= 20:
        ratings = "Bronze"

    elif rank >= 21 and  rank <= 50:
        ratings = "Prata"

    elif rank >= 51 and  rank <= 80:
        ratings = "Ouro"

    elif rank >= 81 and  rank <= 90:
        ratings = "Diamante"
        
    elif rank >= 91 and  rank <= 100:
        ratings = "Lendário"
    else:
        ratings = "Imortal"
    
    print(f"O Herói tem de saldo {rank} vitórias e está no nível {ratings}")

    r = str(input("Deseja consultar o seu rank novamente?(S/N)")).upper().strip()[0]

    if r == "N":
        break
    else:
        continue
