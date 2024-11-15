import gzip
import shutil

# Path to the downloaded .gz file
gz_file_path = 'C:/Users/Kartik Gounder/Downloads/cc.ml.300.vec.gz'
# Path to the extracted .vec file
extracted_file_path = 'D:/cc.ml.300.vec'

# Extract the .gz file
with gzip.open(gz_file_path, 'rb') as f_in:
    with open(extracted_file_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
