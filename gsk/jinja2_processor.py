import sys

import jinja2
from jinja2 import Environment, FileSystemLoader

def create_meta_yaml_from_template(relative_path):
    env = Environment(loader=FileSystemLoader(relative_path))
    template = env.get_template("meta.yaml")
    rendered = template.render()
    with open("%s/meta.yaml" % relative_path, "wb") as f:
        f.write(rendered)


if __name__ == "__main__":
    create_meta_yaml_from_template(sys.argv[1])
