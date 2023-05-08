import re

sequence = "*CACGTGC*AACCAAATT*TACGTTC*TAACGTTC"

abre = re.finditer('[CT]ACGT[GT]C', sequence)



# for item in mos:
#     print(item.group())
#     print(item.span())

