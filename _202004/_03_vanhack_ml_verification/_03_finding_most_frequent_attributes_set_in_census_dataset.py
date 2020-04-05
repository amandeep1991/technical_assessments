################
# Raw Input
# 4
# 0.6
################

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'attributesSet' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER numberOfAttributes
#  2. FLOAT supportThreshold
#

import pandas as pd

df = pd.read_csv('census.csv', header=None)
df.columns = ['age', 'sex', 'education', 'native-country', 'race', 'marital-status', 'workclass', 'occupation',
              'hours-per-week', 'income', 'capital-gain', 'capital-loss']
rows_count = df.shape[0]

unique_filter_criterias = []
selected_filter_criteria = []

for column_name in df.columns:
    unique_filter_criterias.extend(df[column_name].unique())


# print("Unique Filters Count: {}".format(len(unique_filter_criterias)))

def return_filter_count(one_side_rule):
    one_side_rule_conditions = one_side_rule.split(",")
    one_side_rule_filtered_bool_series = pd.Series([True] * rows_count)
    for condition in one_side_rule_conditions:
        new_condition = df[condition.split("=")[0]] == condition
        one_side_rule_filtered_bool_series = one_side_rule_filtered_bool_series & new_condition
    return sum(one_side_rule_filtered_bool_series)


def recursive_picker(current_filter, current_level, current_index, maximum_level, supportThreshold):
    if current_level >= maximum_level:
        # print("11:", [current_filter, current_level, current_index, maximum_level])
        return current_filter
    elif current_index >= len(unique_filter_criterias):
        # print("22:", [current_filter, current_level, current_index, maximum_level])
        return None
    else:
        if current_filter not in "":
            support = return_filter_count(current_filter) / rows_count
            if support < supportThreshold:
                return None
        # print("33:", [current_filter, current_level, current_index, maximum_level])
        new_index = current_index + 1
        while new_index < len(unique_filter_criterias):
            # print("44:", new_index)

            while new_index != len(unique_filter_criterias) and unique_filter_criterias[new_index].split("=")[
                0] in current_filter:
                new_index += 1

            # print("55:", new_index)
            if new_index < len(unique_filter_criterias):
                # print("66:", new_index)
                if current_filter in "":
                    new_filter = unique_filter_criterias[new_index]
                else:
                    new_filter = current_filter + "," + unique_filter_criterias[new_index]
                # print("77:", new_index)
                new_level = current_level + 1
                selected_filter_criteria.append(
                    recursive_picker(new_filter, new_level, new_index, maximum_level, supportThreshold))

                new_index += 1
        # print("1:", selected_filter_criteria)


def attributesSet(numberOfAttributes, supportThreshold):
    global selected_filter_criteria, unique_filter_criterias
    temp_unique_filter_criterias = []
    # print("1:", len(unique_filter_criterias))
    for each_unique_criteria in unique_filter_criterias:
        support = return_filter_count(each_unique_criteria) / rows_count
        if support >= supportThreshold:
            temp_unique_filter_criterias.append(each_unique_criteria)
    unique_filter_criterias = temp_unique_filter_criterias
    # print("2:", len(unique_filter_criterias))
    # print("3:", (unique_filter_criterias))
    output_list = []
    selected_filter_criteria = []
    recursive_picker("", 0, -1, numberOfAttributes, supportThreshold)
    # print("selected_filter_criteria #1:", len(selected_filter_criteria))
    selected_filter_criteria = set(filter(lambda x: x is not None, selected_filter_criteria))
    # print("selected_filter_criteria #2:", len(selected_filter_criteria))
    # print("selected_filter_criteria #3:", (selected_filter_criteria))
    for filter_criteria in selected_filter_criteria:
        support = return_filter_count(filter_criteria) / rows_count
        if support >= supportThreshold:
            output_list.append(filter_criteria)
    return output_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numberOfAttributes = int(input().strip())

    supportThreshold = float(input().strip())

    result = attributesSet(numberOfAttributes, supportThreshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
