#system path?
import sys
#print(sys.path)
#sys.path.append('/path/to/your/module')
sys.path.append(r'C:\myPython\functions')

import mylibrary


x = mylibrary.validateIntegerInput("read x: ", 0)
y = mylibrary.validateIntegerInput("read y: ", 0)
print("gcd = ", mylibrary.gcd(x,y))

