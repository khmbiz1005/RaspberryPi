import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM ) # BCM은  SoC 핀번호로 불러오겠다는 뜻
GPIO.setwarnings( False )

piezo = 13

GPIO.setup( piezo, GPIO.OUT )

try:
    scale = [ 261, 294, 329, 349, 392, 440, 493, 523 ]
    scale2 = [ 1047, 1175, 1319, 1397, 1568, 1761, 1976, 2093 ]

    p = GPIO.PWM( piezo, 100 ) # pulse width modulation 펄스폭 변조. 전압의 on/off를 이용해 가변 전압을 얻는다.
    GPIO.output( piezo, True )
    p.start( 100 ) # 
    p.ChangeDutyCycle( 90 ) # 90% 만 사용한다.
    
    for i in range ( 8 ):
        print( i + 1 )
        p.ChangeFrequency( scale[ i ] ) # 주파수를 변경해준다. 박자는 ChangeDutyCycle 로 조정한다.
        time.sleep(1)
    p.stop()
finally:
    GPIO.cleanup()