# WiringPi モジュールの読み込み
import wiringpi as wpi
# time モジュールの読み込み
import time
# GPIO 番号の設定
LED_Y1 = 13 # 黄色 LED1 GPIO番号13
# GPIO の初期化
wpi.wiringPiSetupGpio()
# GPIO の入出力設定
wpi.pinMode(LED_Y1, wpi.OUTPUT) # GPIO13 を出力に設定
# 黄色 LED1 の点灯
wpi.digitalWrite(LED_Y1, wpi.HIGH)
# 次の処理を 2 秒待つ
time.sleep(2)
# 黄色 LED1 の消灯
wpi.digitalWrite(LED_Y1, wpi.LOW)
