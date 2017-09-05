# with open("scratch.txt", "r") as f:
#     first = f.read()
#
#
# with open("big_env.txt", "r") as i:
#     second = i.read()
#
#
# with open("original.txt", "r") as l:
#     third = l.read()
#
#
# first = set([x.lower() for x in first.split("\n")])
# second = set([x.lower() for x in second.split("\n")])
# third = set([x.lower() for x in third.split("\n")])
#
# print(second - (third | first))

with open("original.txt", "r") as l:
    packages = l.read()

package_list = packages.split("\n")
package_strings = [[x[:x.rfind("_")], x[x.rfind("_") + 1:x.rfind(".tar")]] for x in package_list]
versions = {"name":["r-" + x[0].lower() for x in package_strings], "version":[x[1] for x in package_strings], "available":[]}

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

search_packages()

