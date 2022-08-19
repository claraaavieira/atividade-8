#Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
#A: Veículos com duas ou três rodas;
#B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
#C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
#D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
#E: Veículos com quatro rodas ou mais e com mais de 6000 kg.





rodas = int(input('quantas rodas do veículo tem?'))

peso = (input('qual o peso bruto do veículo?'))
 
pessoas = (input('Há quantas pessoas no veículo?'))

if rodas == 2 or rodas == 3 :
    print('veiculos com duas ou três rodas - CATEGORIA A')
elif rodas == 4 and pessoas <= 8 and peso <= 3500 :
    print('Veículo com quatro rodas que acomoda até oito pessoas e seu peso é de até 3500kg - CATEGORIA B')
elif rodas >= 4 and 3500 <= peso <= 6000 :
    print('Veículo com mais de quatro rodas que acomoda mais de oito pessoas e seu peso é superior a 3500kg e menos de 6000 - CATEGORIA C')
elif rodas >= 4 and pessoas > 8 :
    print('Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas - CATEGORIA B e C')
elif rodas >= 4 and peso > 6000 :
    print('Veículos com quatro rodas ou mais e com mais de 6000 kg - CATEGORIA B, C e D')