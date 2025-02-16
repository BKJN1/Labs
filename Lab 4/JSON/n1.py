import json

with open('sample-data.json') as file:
    data = json.load(file)

print("")
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU ")
print("-------------------------------------------------- --------------------  ------  ------")

for interface in data['imdata']:
    attributes = interface['l1PhysIf']['attributes']
    dn = attributes['dn']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print(f"{dn}                                {speed}   {mtu}")