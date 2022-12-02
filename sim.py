import os
import subprocess
import time
from pathlib import Path

sap = input("Enter your SAP number: ")



cmd = "/home/icomera/pysim/pySim-read.py -p0".split()
while True:
    try:
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE)
        output = p.stdout.read()
        output = output.decode()
        output = output.split("ICCID: ")
        output = output[1]
        output = output.split("\nIMSI")
        output = output[0]
        #print(output)
        if not os.path.exists(f"/home/icomera/{sap}.txt"):
            print("file missing")
            with open(f"/home/icomera/{sap}.txt", "w") as f:
                f.close()
        with open(f"/home/icomera/{sap}.txt") as file:
            if output in file.read():
                exists = True
                #print("iccid exists in file")
                file.close()
            else:
                exists = False
                file.close()
        if exists == False:
            f = open(f'/home/icomera/{sap}.txt', 'a')
            f.write(output+"\n")
            f.close()
            print(f"Wrote ICCID {output} to file")
        time.sleep(1)
    except Exception:
        pass

