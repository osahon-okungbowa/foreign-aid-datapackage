
## DESCRIPTION

This repo contains a data package on Foreign Aid Outflow by Country [OECD] ([see issue](https://github.com/datasets/awesome-data/issues/106)) .

There are numerous datasets to work with from the provided [source](http://www.oecd.org/dac/financing-sustainable-development/development-finance-data/statisticsonresourceflowstodevelopingcountries.htm) . However, we'll focus on [Net Official Development Assistance by DAC Country](http://www.oecd.org/dac/financing-sustainable-development/development-finance-data/TAB04e.xls) as the data source for the package resources

## What The Script Does

 - The script loads the data from the provided source (as an excel file).
 - Excel file contained 2 tables on 1 sheet
 - Script isolates each table and cleans it (removing empty rows, stripping out text content that's not part of the data, correcting column header names etc)
 - Each isolated table is not converted to a data package resource (i.e. we get 2 resources from one Excel sheet)
 - 2 identical data packages are created for the resources (for convenience). first data package container is a directory called *'foreign_aid_package'*, the other package is a zip/archive called *'foreign_aid_package_zip'.*

  

## *PROJECT ENVIRONMENT*

- Python 3.7.6
- Conda Virtual Environment (or any other python virtual environment user prefers)


## *PACKAGE DEPENDENCIES*

The script depends on the following python packages:

- dataflows
- requests
- pandas

All  packages can be installed in the created virtual environment using:

    pip install [package-name]


## *RUNNING THE SCRIPT*

 - clone this repository `git clone https://github.com/osahon-okungbowa/foreign-aid-datapackage.git`
 - create the python virtual environment and activate it
 - change directory into the location of the cloned repository
 - run `python create_package.py`
