##
## EPITECH PROJECT, 2019
## trade_2018
## File description:
## compute
##

def compute_slide_mean(arr, period):
    tmp_array = []
    mean = 0
    for value in arr:
        mean += float(value)
    mean /= period
    return mean

def compute_expo_moving_av(val, period, mme_past, count):
    if count == 1:
        return val
    else:
        a = 2 / (1 + period)
        mme = float(val * a + mme_past * (1 - a))
        return mme