f = open('file1.txt','w+')
f.write('one file')
f.close()

f = open('file2.txt','w+')
f.write('second file')
f.close()

import zipfile

compressed_file = zipfile.ZipFile('comp_file.zip', 'w')
compressed_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
compressed_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')
zip_obj.close()

import shutil
dir_to_zip = './extracted_content'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)

shutil.unpack_archive('example.zip', 'final_unzip', 'zip')