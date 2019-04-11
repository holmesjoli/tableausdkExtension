import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "tableausdkExtension",
    version = "0.0.1.0",
    author = "Joli Holmes",
    author_email = "jh111@rice.edu",
    description = "Tableau for TJJD",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "XXX",
    packages = setuptools.find_packages()
)

