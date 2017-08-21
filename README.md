dex_string_type_classification
------------------------------

Classify the types of DEX strings by machine learning/deep learning.


# 1. Project introduction

The strings in APK DEX files can be extracted. And the strings have different types, such as 'type', 'field_name' and 'method_name'. For example
* the type of string 'addShutdownHook' is `method_name`
* the type of string 'Ljava/util/concurrent/TimeUnit;' is `type`
* the type of string 'total_wait_time' is `field_name`

The target of this project is to classify the types of DEX strings by machine learning/deep learning.


# 2. Dataset construction


* (1) Download apks from http://zhushou.360.cn/ (prefer diversity apps)
   * '360mse_nh00002.apk'
   * 'com.changba_820.apk'
   * 'com.cootek.smartinputv5_5665.apk'
   * 'com.dailyyoga.cn_108.apk'
   * 'com.huajiao_5111011.apk'
   * 'com.lk.wzzj.qh_60.apk'
   * 'com.qiyi.video_80890.apk'
   * 'com.snda.wifilocating_3128.apk'
   * 'com.tencent.reading_3200.apk'
   * 'com.tiange.vshow_24.apk'


* (2) Extract DEX from APK by 7zip


* (3) Extract strings with tag for each DEX file (by internel tool, parse dex format)
   * parse DEX file is very slow (10 min for one dex)
   * androguard also very slow
   
   
* (4) Extracted strings with tag as dict
   
```
{
 'link': set(), # user defined string
 'Observer.onError not implemented and error while unsubscribing.': set(), # user defined string
 'Lorg/jsoup/parser/TokeniserState$37;': {'type'},# variable/object type
 'Ljava/util/jar/JarFile;': {'type'},# variable/object type
 'onFailure': {'method_name'},
 'isExtends': {'field_name', 'method_name'}
}
```

* total 4 types for strings, and multi-types for one string

* dataset 'str_txt/str_dict_com.tiange.vshow_24.dex.jl.txt' saved by python file write directly without format.



# 3. How to run the code

## environment setup



## code structure



## steps to run






# issues

* Multiclass classification: http://scikit-learn.org/stable/modules/multiclass.html
* CNN 
* Unicode support