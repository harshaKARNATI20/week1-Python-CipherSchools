name,ch= input("Enter Comma Seperated Name and character: ").split(",")
print(f'Length of your name: {len(name)}')

#! Case Sensitive
print(f'Sens Character Count: {name.count(ch)}')
#! Case Insensitive
#*Harsha - harsha
#*H  - h
name = name.lower()
ch=ch.lower()
print(f'InSens Character Count: {name.count(ch)}')
#! Space remove strip()
#^ "       Harsha    "--------->    "Harsha"      --------->      "harsha"
#^ "     S      "------->   "H"   --------->   "h"

print(f'Space1 Character Count: {name.replace(" ","").lower().count(ch.replace(" ","").lower())}')
print(f'Space2 Character Count: {name.strip().lower().count(ch.strip().lower())}')

