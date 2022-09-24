from pypresence import Presence
import time
token ="1023109691909353543"
RPC =Presence(token)
RPC.connect()
RPC.update(state="Stu-Dying Jeevan ka aadhar hai",details="Padhle Pehle")

Nikhil = "Sigma"
while Nikhil == "Sigma":
    time.sleep(10)