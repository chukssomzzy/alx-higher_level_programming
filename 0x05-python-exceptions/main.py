#!/usr/bin/python3
import dis
safe_function = __import__('102-magic_calculation').magic_calculation

instt = dis.Bytecode(safe_function)

for inst in instt:
    print(inst.opname)
