"""Initial Setup"""

import threading
import time
import sys
from datetime import datetime
import platform
num = 0

"""Benchmark"""

print(f"Python {sys.version}\nPython version can affect results\nStarting benchmark...")
start_time = datetime.now()
while num < 1000000000 + 1:
    num += 1
end_time = datetime.now()
delta = end_time - start_time
score = delta.total_seconds()
print(f"Benchmark complete!\nScore: {score} (lower is better)")

"""Save Results"""

f = open(f"results-{end_time}.txt", "w")
f.write(f"Score: {score}\nPython ver. {sys.version}\nOS: {platform.system()}\nStart Time: {start_time}\nEnd Time: {end_time}")
f.close()