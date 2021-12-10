import setuptools

setuptools.setup(
    name='battlefish',
    version='0.1',
    description='Allows the user to play battleship against the computer',
    author='Brianna Fernandez',
    author_email='brianna.fernandez@yale.edu',
    include_package_data=True,
    install_requires=[
        'numpy>=1.17',
     ],
     classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Gaming/Entertainment",
        "Operating System :: OS Independent",
        "License :: MIT License",
      ],
    python_requires='>=3.6',
)
