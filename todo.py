import subprocess
import shlex
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
    elif condition == 3:
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
            "build": ""
        })
    return packages


def search_packages(package_list):
    for package in package_list:
        search_string = "conda search --platform linux-64 {}={} --spec {}".format(package["name"], package["version"], CHANNELS)
        result = process_call(search_string)
        if not result[1] and package["name"] in str(result[0]):
            py3 = "py3" in str(result[0])
            py2 = "py27" in str(result[0])
            if package["python2"] and package["python3"]:
                if not (py2 or py3):
                    package["available"] = True
                elif py2 and py3:
                    package["available"] = True
                elif py2 and not py3:
                    package["available"] = False
                    package["build"] = "py3"
                elif py3 and not py2:
                    package["available"] = False
                    package["build"] = "py2"

            if package["python2"] and not py2:
                package["available"] = False
                package["build"] = "py2"
            else:
                package["available"] = True

            if package["python3"] and not py3:
                package["available"] = False
                package["build"] = "py3"
            else:
                package["available"] = True
        else:
            package["available"] = False
            if package["python2"] and package["python3"]:
                package["build"] = "py2py3"
            if package["python2"] and not package["python3"]:
                package["build"] = "py2"
            if package["python3"] and not package["python2"]:
                package["build"] = "py3"
    return package_list


def process_call(command):
    call = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = call.communicate()
    return (result[0], call.returncode)

x = get_package_list(common)
y = get_package_list(py3p, condition=3)
z = get_package_list(py2p, condition=2)
a = x + y + z
writer = pd.ExcelWriter('output.xlsx')
df = pd.DataFrame.from_dict(search_packages(a))
df.to_excel(writer, "Sheet1")
