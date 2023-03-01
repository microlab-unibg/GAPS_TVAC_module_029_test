from os.path import join
import pickle

# Store data with pickle
def store_data(item, item_name, cache_folder):
    outputFile = join(cache_folder, item_name + ".data")
    fw = open(outputFile, "wb")
    pickle.dump(item, fw)
    fw.close()


# Retrieve stored data
def read_data(item_name, cache_folder):
    filepath = join(cache_folder, item_name + ".data")
    fd = open(filepath, "rb")
    dataset = pickle.load(fd)

    return dataset
