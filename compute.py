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