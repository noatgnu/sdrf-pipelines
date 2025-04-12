import codecs
import os.path

with open("README.md", encoding="UTF-8") as fh:
    long_description = fh.read()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__") or line.startswith("version"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


def update_version_in_pyproject(pyproject_file, version):
    updated = False
    new_pyproject_content = ""
    for line in read(pyproject_file).splitlines():
        if line.startswith("version") and not updated:
            delim = '"' if '"' in line else "'"
            new_pyproject_content += f"version = {delim}{version}{delim}\n"
            updated = True
        else:
            new_pyproject_content += line
    with open(pyproject_file, "w") as f:
        f.write(new_pyproject_content)


version_from_init = get_version("sdrf_pipelines/__init__.py")
version_from_pyproject = get_version("pyproject.toml")
if version_from_init != version_from_pyproject:
    update_version_in_pyproject("pyproject.toml", version_from_init)
