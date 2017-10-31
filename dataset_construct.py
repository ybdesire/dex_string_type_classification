import os, pdb
import joblib as jl
from tqdm import *


# run once then get max_len = 2000 manually
def get_string_len_distribution():
    orig_data_path = 'str_txt'
    files = os.listdir(orig_data_path)
    
    # get the string len distribution
    str_len_distribution = {}
    for f in files:
        with open( os.path.join(orig_data_path, f), 'r' ) as fr:
            feadic = eval(fr.read())
            for k in feadic: # key is string
                v = k.encode('raw_unicode_escape')
                str_len = len(v)
                if(str_len not in str_len_distribution):
                    str_len_distribution[str_len] = 0
                str_len_distribution[str_len] += 1
    print(str_len_distribution)
    # {0:16, 50:3292, 228:7, 4044:1}
    # then set max_len for zero-padding

def get_labels_distribution():
    orig_data_path = 'str_txt'
    files = os.listdir(orig_data_path)
    
    # get the string len distribution
    labels_distribution = set()
    for f in files:
        with open( os.path.join(orig_data_path, f), 'r' ) as fr:
            feadic = eval(fr.read())
            for k in feadic:
                labels_distribution.add( tuple(feadic[k]) )# value is label
    print(labels_distribution)
    # {('type',), ('type', 'field_name'), ('method_name', 'type'), ('method_name', 'type', 'field_name'),
    # (), ('method_name',), ('method_name', 'field_name'), ('field_name',)}
    # blank is 'user defined string'



# raw string as feature, max_len, zero-padding
# binary-classification: 
# 1 for user defined string
# 0 for other
def extract_feature_to_dataset_2c():
    dst = 'dataset'
    if not os.path.exists(dst):
        os.makedirs(dst)
    max_len = 1000
    files = os.listdir('str_txt')
    for f in files:
        sid = f.split('_')[2]
        x_dataset = []
        y_dataset = []

        with open( os.path.join('str_txt', f), 'r' ) as fr:
            feadic = eval(fr.read())
            for k in tqdm(feadic): # key is string
                if(k==''):
                    continue # invalid string
                v = k.encode('raw_unicode_escape')
                # set x
                x = [0]*max_len
                if(len(v)<=max_len):
                    x[0:len(v)] = v
                else:
                    x = v[0:max_len]
                # set y
                y = 0
                if(feadic[k]==set()):# type, user defined string
                    y = 1
                # add to dataset
                x_dataset.append(x)
                y_dataset.append(y)
        dataset = {'x':x_dataset, 'y':y_dataset}
        jl.dump(dataset, os.path.join(dst, 'dataset_{0}_xy.jl'.format(sid)))
        print('completed {0}'.format(sid))

if __name__=='__main__':
    extract_feature_to_dataset_2c()



    