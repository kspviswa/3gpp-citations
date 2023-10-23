from setuptools import setup, find_packages

INSTALL_REQUIRE = ["openpyxl==2.4.8",
                   "bibtexparser==0.6.2",
                   "lxml==4.3.1",
                   "requests==2.21.0",
                   "tqdm==4.31.1"]

DESCRIPTION = "This project generates BiBTeX-files for 3GPP specifications. Its a fork from martisak/3gpp-citations from Github"

setup(
    name='sdo-citations',
    author='Viswa Kumar',
    author_email='kspviswaphd@gmail.com',
    version='0.0.1',
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    platforms=['any'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
    ],
    url='https://github.com/kspviswa/3gpp-citations',
    packages=find_packages(),
    license="MIT",
    entry_points={
        'console_scripts': [
            'sdo-citations = standardcitations:process_args',
        ]
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
)
