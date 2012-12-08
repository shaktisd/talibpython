
import numpy as np
strarray = ["535.","535.","534.68"]
floatarray = np.array(filter(None,strarray),dtype='|S10').astype(np.longdouble)
print floatarray