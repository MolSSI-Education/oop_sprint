import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='oop_sprint',
        version="0.1.1",
        description='OOP example at MolSSI summer school',
        author='Doaa Altarawy',
        author_email='daltarawy@vt.edu',
        url="https://github.com/MolSSI-SSS/oop_sprint",
        license='BSD-3C',
        packages=setuptools.find_packages(),

        install_requires=[
            'numpy>=1.7',
        ],

        extras_require={
            'tests': [
                'pytest',
                'codecov',
                'pytest-cov',
                'pytest-pep8',
                'pep8',
            ],
        },


        zip_safe=True,
    )
