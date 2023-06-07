import os

from storage3.utils import StorageException
from supabase import Client

import string
import random


def process_files(folder, supabase_client: Client):
    N = 5
    folder_name = os.path.basename(folder)
    files = os.listdir(folder)
    files = [f for f in files if os.path.isfile(folder + '/' + f)]  # Filtering only the files.

    for file_name in files:
        try:
            supabase_client.storage.from_(folder_name).upload(file_name, os.path.abspath(''.join([folder,'/',file_name])))
        except StorageException as e:
            if 'Duplicate' in e.args[0]['error']:
                random_str = str.join('',random.choices(string.ascii_lowercase + string.digits, k=N))
                new_file_name = ''.join([random_str, file_name])
                supabase_client.storage.from_(folder_name).upload(new_file_name,
                                                                  os.path.abspath(''.join([folder,'/',file_name])))
                file_name = new_file_name

        finally:
            file_list = supabase_client.storage.from_(folder_name).list()
            # check whether the file is uploaded
            for list_item in file_list:
                if list_item.get('name').__eq__(file_name):
                    pass
                    # change the status of data source to COMPLETED
                    # break




