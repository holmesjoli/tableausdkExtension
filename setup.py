import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "tab_tjjd",
    version = "0.0.0.9999",
    author = "Joli Holmes",
    author_email = "jh111@rice.edu",
    description = "Tableau for TJJD",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "XXX",
    packages = setuptools.find_packages()
)

