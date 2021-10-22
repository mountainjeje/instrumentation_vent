# Import de la librairie serial
import serial
import csv

mesure = 0
# Ouverture du port serie avec :
# '/dev/ttyXXXX' : definition du port d ecoute (remplacer 'X' par le bon nom)
# 9600 : vitesse de communication
serialArduino = serial.Serial('/dev/ttyACM0', 9600)
serialArduino.flushInput()

# Ecriture de chaque message recu
while True :
    #print(serialArduino.readline())
    
    print("Ctrl + C to interrupt")

    data = serialArduino.readline()
    print(data)

    decoded_data = list(data.split(", "))
    
    with open('poubelle.csv', 'a') as datalog:
    writer = csv.writer(datalog)
    writer.writerow(decoded_data)
#Condition qui enregistre les mesures lorsqu'on a un vent supérieur à 10m/s en P0 P1 ou P2, ou lorsqu'on a pas enregistré de mesure depuis 60 secondes
    if decoded_data[1]>204 or decoded_data[3]>204 or decoded_data[5]>204 or mesure==60 :
    
        with open('datalog.csv', 'a') as datalog:
        writer = csv.writer(datalog)
        writer.writerow(decoded_data)
        #print("data was written")
        mesure = 0
    
    else :
        mesure = mesure + 1