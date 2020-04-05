################
# Raw Input
# 3
# {native-country=United-States,capital-gain=None}=>{capital-loss=None}
# {capital-gain=None,capital-loss=None}=>{native-country=United-States}
# {native-country=United-States,capital-loss=None}=>{capital-gain=None}
################

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrangingRules' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY rules as parameter.
#

import pandas as pd

df = pd.read_csv('census.csv', header=None)
df.columns = ['age', 'sex', 'education', 'native-country', 'race', 'marital-status', 'workclass', 'occupation', 'hours-per-week', 'income', 'capital-gain', 'capital-loss']
# print(df.head())
rows_count = df.shape[0]

def return_filter_count(one_side_rule):
    one_side_rule_conditions = one_side_rule.split(",")
    one_side_rule_filtered_bool_series = pd.Series([True]*rows_count)
    for condition in one_side_rule_conditions:
        new_condition = df[condition.split("=")[0]]==condition
        one_side_rule_filtered_bool_series = one_side_rule_filtered_bool_series & new_condition
    return sum(one_side_rule_filtered_bool_series)

def arrangingRules(rules):
    # Write your code here
    output_rules = []
    for rule in rules:
        confidence = None
        rule_dependencies = rule.split("=>")
        rows_matching_X_union_Y = return_filter_count(rule_dependencies[0][1:-1]+","+rule_dependencies[1][1:-1])
        rows_matching_X = return_filter_count(rule_dependencies[0][1:-1])
        confidence = rows_matching_X_union_Y/rows_matching_X
        output_rules.append((rule, confidence))
    output_rules_desc = sorted(output_rules, key=lambda x:x[1], reverse=True)
    output_rules_formatted = [ ele[0] for ele in output_rules_desc ]
    return output_rules_formatted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rules_count = int(input().strip())

    rules = []

    for _ in range(rules_count):
        rules_item = input()
        rules.append(rules_item)

    result = arrangingRules(rules)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
