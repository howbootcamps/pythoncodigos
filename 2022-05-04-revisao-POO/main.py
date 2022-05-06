from src.passaro_africano import PassaroAfricano
from src.passaro_europeu import PassaroEuropeu



passaro_africano = PassaroAfricano(1, 1)
passaro_africano_1 = PassaroAfricano(10, 20)

print(passaro_africano.calcula_velocidade())
print(passaro_africano_1.calcula_velocidade())

passaro_africano.incrementa_tempo(10)
passaro_africano.incrementa_distancia(15)

print(passaro_africano.calcula_velocidade())
print(passaro_africano_1.calcula_velocidade())

