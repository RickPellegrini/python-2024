
segundos = int(input('Entre com o valor que gostaria em segundos:'))


horas = segundos // (60*60)

segundos = segundos % (60*60)

minutos = segundos // (60)

segundos = segundos % 60

print (horas, minutos, segundos, sep =':')