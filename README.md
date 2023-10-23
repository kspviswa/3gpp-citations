# SDO Bibtex entry generator

This project aims to generate [BiBTeX](http://www.bibtex.org/) files that
can be used when citing [3GPP](3gpp.org) specifications. The input is a
document list exported from the [3GPP Portal](https://portal.3gpp.org/).

## Installation

`pip install sdo-citations`


## Instructions

1. Go to the [3GPP Portal](https://portal.3gpp.org/#55936-specifications)
1. Generate the list of specifications you want.
1. Download to Excel and save file
1. Run `sdo-citations -i exported.xlsx -o 3gpp.bib`
1. Use in LaTeX.

*Optionally* use the provided `3gpp.bib` directly.

## Things to note

* The output `bibtex` class is set to `@techreport`.
* If you add the option `--xelatex`, break-symbols `\-` will be used in url-fields.
* The version and date are read from 3gpp.org, but it is slow so it takes a while to parse the list. If you find an easy solution to this, let me know.

## Example output

~~~
@techreport{3gpp.36.331,
 author = {3GPP},
 day = {20},
 institution = {{3rd Generation Partnership Project (3GPP)}},
 month = {04},
 note = {Version 14.2.2},
 number = {36.331},
 title = {{Evolved Universal Terrestrial Radio Access (E-UTRA); Radio Resource Control (RRC); Protocol specification}},
 type = {Technical Specification (TS)},
 url = {https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=2440},
 year = {2017}
}
~~~


## Acknowledgment

This project was forked from [martisak/3gpp-citations](https://github.com/martisak/3gpp-citations)
