"""File contains the utility functions used to create the data package i.e.
the resources, meta-data file (datapackage.json) and resource files """

import os
import shutil

import dataflows # pip install dataflows
import requests # pip install requests
import pandas

def load_data(source: str = None) -> dataflows.Flow:
    """Function loads the data specified by the 'source'
    Parameters
    - source: the url/path to load the data from
    """

    # create the directory for storing the downloaded data.
    try:
        os.mkdir('tempdownload')
    except FileExistsError:
        # do nothing
        pass

    # get the datafile name from the provided source
    data_file_name = source[source.rfind('/')+1:]
    # download the data from 'source'
    response = requests.get(source)
    # create a filepath for where the datafile will be stored
    temp_file_path = 'tempdownload/{0}'.format(data_file_name)

    # write the downloaded file to disk
    with open(temp_file_path, 'wb') as tempfile:
        tempfile.write(response.content)

    # read the excel columns containing
    # dac assistance value into panda dataframe
    data_frame_dac_assistance_value = pandas.read_excel(temp_file_path,
                                                        sheet_name=0,
                                                        skiprows=[0, 1, 2, 3],
                                                        usecols='A:H',
                                                        header=0)
    # remove rows with any empty values
    data_frame_dac_assistance_value.dropna(0, how='any',
                                           thresh=None, inplace=True)
    # rename the first column label to 'Country'
    data_frame_dac_assistance_value.rename(columns={'Unnamed: 0': 'Country'},
                                           inplace=True)
    # read the excel columns containing
    # dac assistance GNI percentage into panda dataframe
    data_frame_dac_assistance_gni = pandas.read_excel(temp_file_path,
                                                      sheet_name=0,
                                                      skiprows=[0, 1, 2, 3],
                                                      usecols='J:Q',
                                                      header=0)
    # remove rows with any empty values
    data_frame_dac_assistance_gni.dropna(0, how='any',
                                         thresh=None, inplace=True)
    # rename the first column label to 'Country'
    data_frame_dac_assistance_gni.rename(columns={'Unnamed: 16': 'Country'},
                                         inplace=True)
    # the name of columns have an appended ".1", fix this
    # with list comprehensions
    new_column_names = {column_name:
                        (column_name if column_name.rfind('.1') == -1
                         else column_name[0:column_name.rfind('.1')])
                        for column_name in
                        list(data_frame_dac_assistance_gni.columns.values)}
    # rename the columns after removing the appended ".1"
    data_frame_dac_assistance_gni.rename(columns=new_column_names,
                                         inplace=True)
    # reverse the column names
    # to ensure 'Country' column is in front
    reversed_column_names = list(data_frame_dac_assistance_gni.columns.values)
    reversed_column_names.reverse()
    data_frame_dac_assistance_gni \
        = data_frame_dac_assistance_gni[reversed_column_names]
    # convert the dataframes to csv files
    data_frame_dac_assistance_value.to_csv(
        temp_file_path[0: temp_file_path.rfind('.')] + '.csv',
                index=False, header=True)
    data_frame_dac_assistance_gni.to_csv(
        temp_file_path[0: temp_file_path.rfind('.')] + 'B.csv',
                index=False, header=True)

    # load the data convert csv file and
    # create the Flow objects used to create 'official-dac-value' resource
    # and 'dac-value-gni-percentage' resource
    dac_assistance_value_flow = dataflows.Flow(
        dataflows.load(temp_file_path[0: temp_file_path.
                                      rfind('.')] + '.csv',
                       name='official-dac-values'))
    dac_assistance_gni_flow = dataflows.Flow(
        dataflows.load(temp_file_path[0: temp_file_path.
                                      rfind('.')] + 'B.csv',
                       name='dac-assistance-percentage-gni'))
     # return the flow objects
    return (dac_assistance_value_flow, dac_assistance_gni_flow)


def create_package(flows: tuple = None):
    """Function creates data package.
    Data Packages are created as a folder and also a zip/archive file.
    Parameters
    - flows: tuple which contains the dataflows from which the
    datapackage is created"""

    # run the Flow object that creates the data packages
    dataflows.Flow(*flows,
                   dataflows.dump_to_path(out_path='foreign_aid_package'),
                   dataflows.dump_to_zip(out_file='foreign_aid_package_zip')).\
                       process()

def clean_up_process():
    """Functions clean up after the package making process is completed.
    Specifically, it removes the temp directory and files created"""
    shutil.rmtree('tempdownload')
