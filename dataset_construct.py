import os
import joblib as jl


def extract_feature_to_dataset():
    orig_data_path = 'str_txt'
    files = os.listdir(orig_data_path)
    for f in files:
        with open( os.path.join(orig_data_path, f), 'r' ) as fr:
            feadic = eval(fr.read())
            for k in feadic:
                v = k.encode('raw_unicode_escape').decode('latin-1')



if __name__=='__main__':
    extract_feature_to_dataset()



    