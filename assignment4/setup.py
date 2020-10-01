import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instapy_johancb6", 
    version="0.0.1",
    author="johancb",
    author_email="johancb@uio.no",
    description="a package for changing colors for pictures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.uio.no/IN3110/IN3110-johancb/tree/master/assignment4",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
