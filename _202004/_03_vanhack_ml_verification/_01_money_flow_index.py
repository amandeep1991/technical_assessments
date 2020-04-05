################
# Raw Input
# sample.csv
# 10
################

#!/bin/python3

import math
import os
import random
import re
import sys


# I can do this using pandas as well, but willing to show that I know underlying code [obviously, it can't be compared with efficient pandas code, but just to showcase the approach]

# Complete the moneyFlowIndex function below.
def moneyFlowIndex(filename, n):
    output_file = open("money_flow_index_{n}.csv".format(n=n), "w")
    output_line = (
        "Day,Open,High,Low,Close,Volume,Typical Price,Positive Money Flow,Negative Money Flow,Positive Money Flow Sum,Negative Money Flow Sum,Money Flow Index")
    output_file.write(output_line + "\n")
    typical_price_new = None
    positive_flow_array = []
    negative_flow_array = []
    input_file = open(filename, 'r')
    lines = input_file.read().split("\n")
    for index, line in enumerate(lines[1:-1], start=1):
        output_line = line
        elements_array = line.split(",")
        try:
            high, low, close = float(elements_array[2]), float(elements_array[3]), float(elements_array[4])
        except Exception as e:
            print("ERROR::", elements_array)
            raise e
        volume = float(elements_array[5])
        typical_price_temp = typical_price_new
        typical_price_new = (high + low + close) / 3

        output_line += (",{}".format(round(typical_price_new, 6)))
        if typical_price_temp is not None:
            positive_or_negative_flow = volume * typical_price_new
            if len(positive_flow_array) == n or len(negative_flow_array) == n:
                if len(positive_flow_array) == n and len(negative_flow_array) == n:
                    positive_flow_array = positive_flow_array[1:]
                    negative_flow_array = negative_flow_array[1:]
                else:
                    raise ValueError("Error in array setups")
            if typical_price_temp == typical_price_new:
                continue
            elif typical_price_temp < typical_price_new:
                positive_flow_array.append(positive_or_negative_flow)
                negative_flow_array.append(0)
                output_line += (",{}".format(round(positive_or_negative_flow, 6)))
                output_line += (",")

            else:
                positive_flow_array.append(0)
                negative_flow_array.append(positive_or_negative_flow)
                output_line += (",")
                output_line += (",{}".format(round(positive_or_negative_flow, 6)))
            if len(positive_flow_array) == n and len(negative_flow_array) == n:
                positive_money_flow_sum = sum(positive_flow_array)
                negative_money_flow_sum = sum(negative_flow_array)
                output_line += (",{}".format(round(positive_money_flow_sum, 6)))
                output_line += (",{}".format(round(negative_money_flow_sum, 6)))
                money_ratio = positive_money_flow_sum / negative_money_flow_sum
                money_flow_index = ((money_ratio) / (1 + money_ratio)) * 100
                output_line += (",{}".format(round(money_flow_index, 6)))
            else:
                output_line += (",")
                output_line += (",")
                output_line += (",")


        else:
            output_line += (",,,,,")

        output_file.write(output_line)
        output_file.write("\n")

    output_file.close()
    file_output = open("money_flow_index_{n}.csv".format(n=n), "r").read()
    # import re
    # print(re.findall("\.\d{7,}", file_output))
    # print(file_output)


if __name__ == '__main__':
    filename = input()

    n = int(input())

    moneyFlowIndex(filename, n)
