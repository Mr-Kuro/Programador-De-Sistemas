# class Tv:
#     def __init__(self, initVolume, initCanal):
#         self.volume = initVolume
#         self.canal = initCanal
#
#     def volumar(self, volume):
#         if volume > 100:
#             print('volume máximo alcansado')
#         else:
#             while 100 > volume > 0:
#                 self.volume += volume
#                 if self.volume == 0:
#                     print('volume mínimo alcansado')
#                     break
#                 elif self.volume > 100:
#                     print('volume máximo alcansado')
#                     break
#
#     def canalar(self, canal):
#         if 100 < canal < 0:
#             print('canal não encontrado')
#         else:
#             while self.canal > canal:
#                 self.volume += 1
#                 break
#
#     def getCanal(self):
#         return self.canal
#
#     def getVolume(self):
#         return self.volume
#
#
# volume = 1
# canal = 1
#
# televisao = Tv(volume, canal)
#
# print(f'\nVolume - {televisao.getVolume()}')
# print(f'Canal  - {televisao.getCanal()}\n')
#
# condicao = 'sim'
# while condicao.lower() == 'sim':
#     print('Deseja aumentar o volume?')
#     pVolume = input()
#     if pVolume.lower() == 'sim':
#         print(f'O volume é de {televisao.getVolume()}. Mínimo 0, máximo 100\n'
#               f'Digite quanto deseja aumentar do volume ou diminuir:')
#         rVolume = float(input())
#         televisao.volumar(rVolume)
#
#     print('Deseja mudar de canal?')
#     pCanal = input()
#     if pCanal.lower() == 'sim':
#         print(f'O canal atual é {televisao.getCanal()}. Mínimo 0, máximo 100\n'
#               f'Digite o canal para onde quer ir:')
#         rCanal = float(input())
#         televisao.canalar(rCanal)
#
#     print('Deseja fazer mais alterações no volume ou mudar o canal da televisão?')
#     condicao = input()
#
# print(f'\nVolume - {televisao.getVolume()}')
# print(f'Canal  - {televisao.getCanal()}')
# print("\nAlteraçõe concluidas! Fim da operação")

# resolução do professor

class Tv:

    def __init__(self):
        self.volume = 0
        self.canal = 0

    def setCanal(self, canal):
        if (canal >= 0) and (canal <= 100):
            self.canal = canal

    def aumentaVolume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuiVolume(self):
        if self.volume > 0:
            self.volume -= 1

canal = 10
tvSala = Tv()
tvSala.setCanal(canal)
tvSala.setCanal(canal)
print(tvSala.canal)

print(tvSala.volume)
tvSala.aumentaVolume()
print(tvSala.volume)

tvSala.diminuiVolume()
print(tvSala.volume)
