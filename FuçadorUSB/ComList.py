import serial 

lines = [ 'M82\n'] 
nLine = 1

COMP = serial.Serial( "COM7", baudrate = 115200 )

for line in lines:
    COMP.write( line.encode() )
    while True:
        read = COMP.readline()
        print( 'Linha', nLine, '/ Enviado:', line, '/ Recebido :', read ) 
        if b'ok' in read:
            nLine += 1 
            break
