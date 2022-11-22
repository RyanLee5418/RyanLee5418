# Creator: Ruowei Li
# Email: lir3@tcd.ie
import numpy as np
import my_median
import scipy
from scipy import signal

l = int(input("Please enter the filter length:"))
if (l % 2) == 0:
    print("{0} is an even number, please try again and enter a odd number".format(l))
else:
    in_l1 = input("Please enter a list:")
    in_l1 = in_l1.strip('[')
    in_l1 = in_l1.strip(']')
    in_l = in_l1.split(',')
    in_l = [int(in_l[i]) for i in range(len(in_l))]
    t_l = in_l
    Test_l = scipy.signal.medfilt(t_l, l)
    print("The correct result list is:")
    print(Test_l)
    print("The filtered list is:")
    my_median.my_median(l, in_l)
