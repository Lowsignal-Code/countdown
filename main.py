"""Quick countdown timer. Usage: python countdown.py 10"""

import sys
import time

seconds = int(sys.argv[1]) if len(sys.argv) > 1 else 60

try:
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{mins:02d}:{secs:02d}", end="", flush=True)
        time.sleep(1)
        seconds -= 1

    print("\rTime's up!      ")
except KeyboardInterrupt:
    print("\nStopped.")