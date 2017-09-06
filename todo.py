import subprocess
import pandas as pd


CHANNELS = "-c glaxosmithkline -c defaults -c r"


with open("py2k.txt", "r") as f:
    py2 = f.read()

with open("py3k.txt", "r") as i:
    py3 = i.read()

py2_packages = py2.split("\n")
py3_packages = py3.split("\n")
common = list(set(py2_packages) & set(py3_packages))
py2p = list(set(py2_packages) - set(py3_packages))
py3p = list(set(py3_packages) - set(py2_packages))


def get_package_list(package_list, condition=32):
    if condition == 32:
        py3 = True
        py2 = True
    elif condition == 2:
        py3 = False
        py2 = True
    elif condition is 3:
        py3 = True
        py2 = False
    else:
        assert 0
    packages = []
    for package_name in package_list:
        packages.append({
            "name": package_name.split("==")[0].lower(),
            "version": package_name.split("==")[-1],
            "available": False,
            "python3": py3,
            "python2": py2,
        })
    return packages


def search_packages(package_list):
    for x in package_list:
        search_string = "conda search --platform linux-64 {}={} --spec {}".format(x["name"], y["version"], CHANNELS)
        result = process_call(search_string)


def process_call(command):
    subprocess.Popen()
    call = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = call.communicate()
    return (result[0], call.returncode)

x = get_package_list(common)
y = get_package_list(py3p, condition=3)
z = get_package_list(py2p, condition=2)
a = x + y + z
# search_packages()
