import subprocess
import pandas as pd


with open("py2k.txt", "r") as f:
    py2 = f.read()

with open("py3k.txt", "r") as i:
    py3 = i.read()

py2_packages = py2.split("\n")
py3_packages = py3.split("\n")

def get_package_strings(package_list):
    return [[x[:x.rfind("_")], x[x.rfind("_") + 1:x.rfind(".tar")]] for x in package_list]

versions = {
    "name":["r-" + x[0].lower() for x in package_strings],
    "version":[x[1] for x in package_strings],
    "available":[]
}

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

# search_packages()
