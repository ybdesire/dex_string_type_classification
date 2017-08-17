# dex_string_type_classification
Classify the types of DEX strings by machine learning/deep learning.


# Project introduction

The strings in APK DEX files can be extracted. And the strings have different types, such as 'type', 'field_name' and 'method_name'. For example
* the type of string 'addShutdownHook' is `method_name`
* the type of string 'Ljava/util/concurrent/TimeUnit;' is `type`
* the type of string 'total_wait_time' is `field_name`

The target of this project is to classify the types of DEX strings by machine learning/deep learning.




# How to run the code

## environment setup



## code structure



## steps to run






# issues

* Multiclass classification: http://scikit-learn.org/stable/modules/multiclass.html
* CNN 
* Unicode support