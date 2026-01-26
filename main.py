import os
from datetime import datetime

Test = input("Which the name file")

now = datetime.now()
date = now.strftime("%Y-%m-%d")

os.makedirs(date, exist_ok=True)

print("Pasta criada:", date)
