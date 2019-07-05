from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name="zermelo.py",
  version="0.0.4",

  description="Zermelo api wrapper library for python.",
  long_description=long_description,
  long_description_content_type="text/markdown",

  py_modules=["zermelo"],
  package_dir={"zermelo": "zermelo"},

  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Operating System :: OS Independent",
  ]
)
