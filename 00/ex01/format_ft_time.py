import time
from datetime import datetime

t = time.time()
print("Seconds since January 1, 1970:", t, " or ", "{:e}".format(t), " in scientific notation")
date_str = datetime.now().strftime("%b %d, %Y")
# %B pour le mois en toutes lettres
print(date_str)
