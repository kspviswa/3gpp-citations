from setuptools import setup, find_packages

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
    scripts=['bin/sdo-citations'],
    install_requires=["bibtexparser==1.4.1",
                      "certifi==2023.7.22",
                      "charset-normalizer==3.3.1",
                      "et-xmlfile==1.1.0",
                      "idna==3.4",
                      "jdcal==1.4.1",
                      "lxml==4.9.3",
                      "openpyxl==2.4.8",
                      "pyparsing==3.1.1",
                      "requests==2.31.0",
                      "tqdm==4.66.1",
                      "urllib3==2.0.7"],
    python_requires=">=3",
)
