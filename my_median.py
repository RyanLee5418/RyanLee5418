# Creator: Ruowei Li
# Email: lir3@tcd.ie
import numpy as np


def my_median(l, inlist):

    l_p = (l - 1) / 2
    l_p0 = int(l_p)
    i = 0
    j = 0

    fl_list = []

    while i < l_p0:
        inlist.insert(0, 0)
        inlist.insert(len(inlist) + l_p0 - 1, 0)
        i += 1

    while j < len(inlist) - l + 1:
        md_wd = inlist[j: j + l]
        md_wd.sort()
        media_n = md_wd[l_p0]
        fl_list.append(media_n)

        j += 1
        md_wd = []

    print(fl_list)
