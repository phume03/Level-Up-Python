#! /usr/bin/env python
# @author: Phumelela Mdluli
# @date: 25 July 2023
# @name: Running Averages
# @description: produces a list of tuples where each tupple is the independent variable, the dependent variable, and the running average of the dependent variable.
# @python version: 3.11
import string
from decimal import *

# France 20 years unemployment data: Unemployment, total (% of total labor force) (modeled ILO estimate)
year = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
unemployment = [8.31,8.91,8.49,8.45,7.66,7.06,8.74,8.87,8.81,9.4,9.92,10.29,10.35,10.05,9.41,9.02,8.41,8.01,7.86,7.445]

def running_average(stats: list):
    sum = 0
    running_avg = []
    for index, figure in enumerate(unemployment, start=1):
        sum = sum + figure
        running_avg.append(float(Decimal(sum / index).quantize(Decimal('.01'), rounding=ROUND_DOWN)))
        pass
    return running_avg

def stat_tuple(*args: list):
    return list(zip(*args))

if __name__ == "__main__":
    print(f'Printing sample running averages tuples...')
    print(f'Data coding: [(year, unemployment %, unemployment running avg %), ...]')
    running_avg = running_average(unemployment)
    final_data = stat_tuple(year, unemployment, running_avg)
    print(f'Output: {final_data}')
    pass
