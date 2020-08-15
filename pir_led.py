import RPi.GPIO as GPIO
import time
import led2 as LED

pir = 24

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( False )

GPIO.setup( pir, GPIO.IN )

led1 = 14

GPIO.setup( led1, GPIO.OUT )
LED.led_init( LED.led1, LED.led2 )
LED.led_off( LED.led1, LED.led2 )
LED.led_init( LED.led1, LED.led2 )


def led_on( led1 ):
    GPIO.output( led1, True )

def led_off( led1 ):
    GPIO.output( led1, False )

def loop():
    cnt = 0
    while True:
        if (GPIO.input( pir ) == True ):
            print( 'detected {}'.format( cnt ) )
            cnt += 1
            led_on( led1 )
            time.sleep( 0.1 )
        elif (GPIO.input( pir ) == False ):
            led_off( led1 )
        time.sleep( 0.1 )


try:
    loop()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()