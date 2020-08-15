import RPi.GPIO as GPIO
import time

trig = 0 # transmit
echo = 1 # receive

GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( False )

GPIO.setup( trig, GPIO.OUT ) # in/out set together
GPIO.setup(echo, GPIO.IN )

try:
    while True:
        GPIO.output( trig, False )
        time.sleep( 0.5 )
        
        GPIO.output( trig, True )
        time.sleep( 0.00001 )

        GPIO.output( trig, False )

        while GPIO.input( echo ) == False : # false면 start 시간을 갱신한다  아니면 while을 빠져나간다.
            pluse_start = time.time() # 수신이 안된 시점의 시작시간을 잡는것.

        while GPIO.input( echo ) == True: # True면 빠져나간다는 뜻.
            pluse_end = time.time()

        pluse_duration = pluse_end - pluse_start
        distance = pluse_duration * 17000
        distance = round( distance )

        print( 'Distance : {:.2f}cm'.format( distance ) )
except KeyboardInterrupt:
    pass