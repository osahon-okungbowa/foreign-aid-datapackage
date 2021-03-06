"""File is the main script to run in order to create the package.
i.e. this is the entry point of the process.
The package contains 2 resource file obtained from a single excel sheet."""

import data_package_utilities as dpu

# script execution begin here
if __name__ == "__main__":
    # store the url of the data to be downloaded & coverted to a data package
    DATA_URL = "http://www.oecd.org/dac/financing-sustainable-development/" +\
               "development-finance-data/TAB04e.xls"
    # load the data and store the process flows
    print('loading data from source...')
    DATA_FLOWS = dpu.load_data(DATA_URL)
    # create the data package
    print('data loaded.')
    print('creating resource files and data package...')
    print('2 data packages will be created.... ')
    print('one is a directory called "foreign_aid_package"...')
    print('two is a zip/archive called "foreign_aid_package_zip"...')
    dpu.create_package(DATA_FLOWS)
    print('data package created.')
    # cleanup process
    print('cleaning up...')
    dpu.clean_up_process()
    print('clean up completed')
    print('DATA PACKAGE CREATED SUCCESSFULLY')
