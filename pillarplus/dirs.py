""" 
    Here files staorage will be defind as a sepeerate module
"""


def upload_csv_files(instance,filename):
    return 'csv/{0}/file/{1}'.format(instance.csv_file,filename)

