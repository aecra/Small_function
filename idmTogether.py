import os

idm_download_file_folder = 'F:/Users/aecra/Desktop/idmFrom/'

idm_to_file = 'F:/Users/aecra/Desktop/idmFrom.ef2'


for file in os.listdir(idm_download_file_folder):
    print(idm_download_file_folder + file)
    f = open(idm_download_file_folder + file)
    f2 = open(idm_to_file, 'a')
    content = f.read()
    f2.write(content)
