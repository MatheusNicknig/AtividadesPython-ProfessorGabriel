tempo_gasto = int(input('Quanto tempo durou a viagem (horas): '))
velocidade_media = int(input('Qual foi a velocidade media da viagem(Em km/h): '))
distancia = tempo_gasto * velocidade_media
litros = distancia /12
print(f'Seu tempo gasto foi de: {tempo_gasto}horas, sua velocidade média foi de: {velocidade_media}km/h, sua distância foi de: {distancia}km e sua quantidade de litros gasta foi de: {litros} litros')