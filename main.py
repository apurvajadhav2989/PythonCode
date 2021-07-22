import platform
import os
os=os.uname()
print(os)

achitecture=platform.architecture()
print(achitecture)

node=platform.node()
print(node)

ver=platform.version()
print(ver)
sys=platform.system()
print(sys)
proc=platform.processor()
print(proc)

mc=platform.machine()
print(mc)

