from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name="zermelo.py",
  version="1.0",
  license="MIT",
  url="https://github.com/wouter173/zermelo.py",

  description="Zermelo api wrapper library for python.",
  long_description=long_description,
  long_description_content_type="text/markdown",

  py_modules=["zermelo"],
  package_dir={"zermelo": "zermelo"},
  install_requires=["requests>=2.17.0"],

  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Development Status :: 1 - Planning",
  ]
)
