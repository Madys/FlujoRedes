import os

paquete="seaborn"
while True:
    try:
        codigo='pip install '+paquete
        os.system(codigo)
        print ('paquete instalado')
    except:
        print('error al instalar')
    continuar=input ('quiere instalar otro')
    continuar=str(continuar)     
    if continuar=='S' or continuar=='s':
        paquete=input('new paquete a instalar')
        paquete=str(paquete)
    else:
        break
print('fin')
