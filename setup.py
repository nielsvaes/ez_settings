import sys
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ez_settings",
    version="1.0.0",
    author="Niels Vaes",
    author_email="niels.vaes@gmail.com",
    description="Easy settings for python applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nielsvaes/ez_settings",
    install_requires=[],
    packages=setuptools.find_packages(),
    classifiers=[
        "Operating System :: OS Independent",
    ]
)