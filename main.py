import platform
import os
os=os.uname()
print(os)

achitecture=platform.architecture()
print(achitecture)

mc=platform.node()
print(mc)

ver=platform.version()
print(ver)
sys=platform.system()
print(sys)
proc=platform.processor()
print(proc)
