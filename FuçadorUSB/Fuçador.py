import serial 
import os 

PATH  = os.path.dirname( __file__ )
MODEL = 'Battery_case.gcode'
PORT  = 'COM7'
BAUD  = 115200

COMP = serial.Serial( PORT, baudrate = BAUD )

nLine = 0 
with open( PATH + '/Modelos/' + MODEL, 'r' ) as f:
    for line in f.readlines():
        line = line.split(';')[0]
        if line:
            COMP.write( (line + '\r\n').encode() )
            print("Escrevendo :", line )    
            while True:
                read = COMP.readline()
                print( 'Linha', nLine, '/ Enviado:', line, '/ Recebido :', read ) 
                if b'ok' in read:
                    nLine += 1 
                    break