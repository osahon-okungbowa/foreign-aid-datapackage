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
    DATA_FLOWS = dpu.load_data(DATA_URL)
    # create the data package
    dpu.create_package(DATA_FLOWS)
    # cleanup process
    dpu.clean_up_process()
