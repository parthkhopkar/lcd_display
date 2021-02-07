import sys
import time
import signal
import lcd_display as ld
from datetime import datetime

def signal_handler(signum, frame):
    print('Turning display off...')
    mylcd.lcd_clear()
    mylcd.backlight(0)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

mylcd = ld.lcd()
mylcd.lcd_clear()
mylcd.lcd_display_string('Hello, World!', 1)
mylcd.lcd_display_string('Parth\'s Raspberry Pi', 4)

while True:
    mylcd.lcd_display_string(datetime.now().strftime('%I:%M %p'), 2)
    time.sleep(0.001)
