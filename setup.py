from setuptools import setup, find_packages

setup(
    name='common-sense',
    version='0.1.0',
    description='Because common sense is not so common. Now it is — in Python!',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Happy Sharma",
    author_email="happycse54@gmail.com",
    url='https://github.com/Happy-Kumar-Sharma/common-sense',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.7',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
