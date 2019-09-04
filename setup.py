import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="zermelo.py",
  version="1.0.1",
  license="MIT",
  url="https://github.com/wouter173/zermelo.py",

  description="Zermelo api wrapper library for python.",
  long_description=long_description,
  long_description_content_type="text/markdown",

  package_dir={"zermelo": "zermelo"},
  install_requires=["requests>=2.17.0"],

  packages=setuptools.find_packages(),

  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: MIT License",
    "Development Status :: 5 - Production/Stable",
  ]
)
