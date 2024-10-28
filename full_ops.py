# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv.
#
# Written by Alwaleed Alrashidi 
# Other contributors: Prof Brad Denby (Boilerplate and lecture slide refernce code)
#

# import Python modules
# e.g., import math # math module

import sys # argv
import math

if len(sys.argv)==3:
  c_in = float(sys.argv[1])
  n_wv = float(sys.argv[2])
else:
  print(\
   'Usage: '\
   'python3 conv_ops.py c_in n_wv'\
  )
  exit()


c_out = n_wv  
h_out = 1  
w_out = 1  

adds = c_in*n_wv  
muls = c_in*n_wv 
divs = 0  


print(int(c_out)) 
print(int(h_out))  
print(int(w_out))  
print(int(adds))   
print(int(muls))  
print(int(divs))   