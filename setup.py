import os
import re

from setuptools import find_packages, setup


def get_extra_requires(path, add_all=True):
    import re
    from collections import defaultdict

    with open(path) as fp:
        extra_deps = defaultdict(set)
        for k in fp:
            if k.strip() and not k.startswith("#"):
                tags = set()
                if ":" in k:
                    k, v = k.split(":")
                    tags.update(vv.strip() for vv in v.split(","))
                tags.add(re.split("[<=>]", k)[0])
                for t in tags:
                    extra_deps[t].add(k)

        # add tag `all` at the end
        if add_all:
            extra_deps["all"] = set(vv for v in extra_deps.values() for vv in v)

    return extra_deps


regexp = re.compile(r".*__version__ = [\'\"](.*?)[\'\"]", re.S)

base_package = "superconfig"
base_path = os.path.dirname(__file__)

init_file = os.path.join(base_path, "src", "superconfig", "__init__.py")
with open(init_file, "r") as f:
    module_content = f.read()

    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError("Cannot find __version__ in {}".format(init_file))

with open("README.rst", "r") as f:
    readme = f.read()

with open("CHANGELOG.rst", "r") as f:
    changes = f.read()


def parse_requirements(filename):
    """Load requirements from a pip requirements file"""
    with open(filename, "r") as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines


requirements = parse_requirements("requirements.txt")


if __name__ == "__main__":
    setup(
        name="Super-Config",
        description="Config parsing on steroids",
        long_description="\n\n".join([readme, changes]),
        license="Apache Software License 2.0",
        url="https://github.com/ajkdrag/Super-Config",
        version=version,
        author="ajkdrag",
        author_email="",
        maintainer="ajkdrag",
        maintainer_email="",
        install_requires=requirements,
        extras_require=get_extra_requires("extra-requirements.txt"),
        keywords=["superconfig", "Super-Config", "Super_Config", "super_config"],
        package_dir={"": "src"},
        packages=find_packages("src"),
        zip_safe=False,
        classifiers=[
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
    )
