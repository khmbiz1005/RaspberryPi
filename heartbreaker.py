# airplane song or heartbreaker

import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( False )


piezo = 13
# hz = { 'do':261, 're': 293.6648, 'mi':329.6276, 'fa':349.2282, 'sol':391.9954, 'la':441.0000, 'si':493.8833 } airplane song
# scores = ( ''sol','sol','la','la', 'sol','sol','mi','sol','sol','mi','mi','re'' ) airplane song

hz = { 'mi': 1244.508, 'fa': 1396.913, 'sol': 1567.982, 'fa2': 1318.510  } # otcta 6
# hz = { 'mi': 622.2540, 'fa': 698.4565, 'sol': 1567.982, 'la':415.3047, 'si':466.1638 }
scores = ( 'mi','fa','sol','sol','sol','sol','sol','sol','fa','mi' )

GPIO.setup( piezo, GPIO.OUT )
p = GPIO.PWM( piezo, 100 )
p.start ( 50 )
# p.ChangeDutyCycle( 10 )

try:
    for scale in scores:
        p.ChangeFrequency(hz[ scale ] )
        time.sleep(0.25)

except : 
    print( 'Exception...' )

finally:
    p.stop()
    GPIO.cleanup()