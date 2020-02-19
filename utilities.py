"""File contains the utility functions used to create the data package i.e.
the resources, meta-data file (datapackage.json) and resource files """

import dataflows # pip install dataflows


def load_data(source=None) -> dataflows.Flow:
    """Function loads the data specified by the 'source'
    Parameters
    - source: the url/path to load the data from
    """

    # load the data specified & create the Flow object used for data packaging
    process_flow = dataflows.Flow(dataflows.
                                  load(source,
                                       name='official-development-assistance'))
    return process_flow # return the flow object


def create_package(flow):
    """Function creates data package"""
    dataflows.Flow(flow, dataflows.dump_to_path(out_path='foreign_aid')).process()

if __name__ == "__main__":
    data_flow = load_data(
        "http://www.oecd.org/dac/financing-sustainable-development/" +
        "development-finance-data/TAB04e.xls")
    create_package(data_flow)
