from setuptools import setup

setup(
  name="png2jpg",
  version="1.0",
  description="all we need are jpgs",
  author="Erik Bernoth",
  author_email="erik.bernoth@gmail.com",
  url="https://github.com/Play2Learn-Org/png2jpg",
  py_modules=["png2jpg"],
  entry_points= {
    'console_scripts' : [
      'png2jpg = png2jpg:main',
    ],
  },
  install_requires=[
    "Pillow>=9.3.0",
  ],
  provides=[
    "png2jpg (1.0)",
  ],
)
