# Import de la librairie serial
import serial
import csv

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
    
    with open('datalog.csv', 'a') as datalog:
        writer = csv.writer(datalog)
        writer.writerow(decoded_data)
        #print("data was written")
