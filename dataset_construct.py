import os
import joblib as jl


def extract_feature_to_dataset():
    orig_data_path = 'str_txt'
    files = os.listdir(orig_data_path)
    
    # get the string len distribution
    str_len_distribution = {}
    for f in files:
        with open( os.path.join(orig_data_path, f), 'r' ) as fr:
            feadic = eval(fr.read())
            for k in feadic:
                v = k.encode('raw_unicode_escape')
                str_len = len(v)
                if(str_len not in str_len_distribution):
                    str_len_distribution[str_len] = 0
                str_len_distribution[str_len] += 1
    print(str_len_distribution)
    # {0:16, 50:3292, 228:7, 4044:1}
    # then set max_len for zero-padding
    
    
    

if __name__=='__main__':
    extract_feature_to_dataset()



    