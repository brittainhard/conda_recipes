import subprocess
import pandas as pd


with open("py2k.txt", "r") as f:
    py2 = f.read()

with open("py3k.txt", "r") as i:
    py3 = i.read()

py2_packages = py2.split("\n")
py3_packages = py3.split("\n")
common = list(set(py2_packages) & set(py3_packages))
py2p = list(set(py2_packages) - set(py3_packages))
py3p = list(set(py3_packages) - set(py2_packages))


def get_package_strings(package_list, condition=32):
    package_dict = []
    for package_name in package_list:
        package_dict.append({
            "name": package_name.split("==")[0].lower(),
            "version": package_name.split("==")[-1],
            "condition": condition,
            "available": False
        })
    return package_dict

# versions = {
#     "name":["r-" + x[0].lower() for x in package_strings],
#     "version":[x[1] for x in package_strings],
#     "available":[]
# }

def search_packages():
    for x, y in zip(versions["name"], versions["version"]):
        search_string = "conda search {}={} --spec".format(x, y)
        is_available = process_call(search_string)
        if is_available == 1:
            versions["available"].append(False)
        elif is_available == 0:
            versions["available"].append(True)


def process_call(search_string):
    return subprocess.call(shlex.split(search_string))

x = get_package_strings(common)
y = get_package_strings(py3p, condition=3)
z = get_package_strings(py2p, condition=2)
a = x + y + z
# search_packages()
