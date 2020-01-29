import re


def compare_versions(version_1: str, version_2: str, splitter: str = r"\.") -> int:
    version_1_list = re.split(splitter, version_1)
    version_2_list = re.split(splitter, version_2)
    for v1, v2 in zip(version_1_list, version_2_list):
        assert not (v1.isnumeric() ^ v2.isnumeric()), "ERROR: Provided versions are incompatible << because '{}' can't be compared with '{}' >> ".format(v1, v2)
        if v1.isnumeric():
            v1 = int(v1)
            v2 = int(v2)
        if v1 < v2:
            return -1
        elif v1 == v2:
            continue
        else:
            return 1
    no_of_components_in_version_1 = len(version_1_list)
    no_of_components_in_version_2 = len(version_2_list)
    if no_of_components_in_version_1 == no_of_components_in_version_2:
        return 0
    elif no_of_components_in_version_1 > no_of_components_in_version_2:
        return 1
    else:
        return -1
