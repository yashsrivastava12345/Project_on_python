
#import pandas as pd
import numpy as np
l=[[[[1,2,3,4],[11,12,13,14],[21,22,23,24],[31,32,33,34]],[[101,102,103,104],[111,112,113,114],[121,122,123,124],[131,132,133,134]],[[201,202,203,204],[211,212,213,214],[212,222,223,224],[231,232,233,234]],[[301,302,303,304],[311,312,313,314],[321,322,323,324],[331,332,333,334]]],\
    [[[1001,1002,1003,1004],[1011,1012,1013,1014],[1021,1022,1023,1024],[1031,1032,1033,1034]],[[1101,1102,1103,1104],[1111,1112,1113,1114],[1121,1122,1123,1124],[1131,1132,1133,134]],[[1201,1202,1203,1204],[1211,1212,1213,1214],[1212,1222,1223,1224],[1231,1232,1233,1234]],[[1301,1302,1303,1304],[1311,1312,1313,1314],[1321,1322,1323,1324],[1331,1332,1333,1334]]],\
    [[[2001,2002,2003,2004],[2011,2012,2013,2014],[2021,2022,2023,2024],[2031,2032,2033,2034]],[[2101,2102,2103,2104],[2111,2112,2113,114],[2121,2122,2123,2124],[2131,2132,2133,2134]],[[2201,2202,2203,2204],[2211,2212,2213,2214],[2212,2222,2223,2224],[2231,2232,2233,2234]],[[2301,2302,2303,2304],[2311,2312,2313,2314],[2321,2322,2323,2324],[2331,2332,2333,2334]]],\
    [[[3001,3002,3003,3004],[3011,3012,3013,3014],[3021,3022,3023,3024],[3031,3032,3033,3034]],[[3101,3102,3103,3104],[3111,3112,3113,3114],[3121,3122,3123,3124],[3131,3132,3133,3134]],[[3201,3202,3203,3204],[3211,3212,3213,3214],[3212,3222,3223,3224],[3231,3232,3233,3234]],[[3301,3302,3303,3304],[3311,3312,3313,3314],[3321,3322,3323,3324],[3331,3332,3333,3334]]]]

l1=[[[[10001,10002,10003,10004],[10011,11002,10013,10014],[10021,10022,10023,10024],[10031,10032,10033,10034]],[[10101,10102,10103,10104],[10111,10112,10113,10114],[10121,10122,10123,10124],[10131,10132,10133,10134]],[[10201,10202,10203,10204],[10211,10212,10213,10214],[10212,10222,10223,10224],[10231,10232,10233,10234]],[[10301,10302,10303,10304],[10311,10312,10313,10314],[10321,10322,10323,10324],[10331,10332,10333,10334]]],\
    [[[11001,11002,11003,11004],[11011,11012,11013,11014],[11021,11022,11023,11024],[11031,11032,11033,11034]],[[11101,11102,11103,11104],[11111,11112,11113,1114],[11121,11122,11123,11124],[11131,11132,11133,11134]],[[11201,11202,11203,11204],[11211,11212,11213,11214],[11212,11222,11223,11224],[11231,11232,11233,11234]],[[11301,11302,11303,11304],[11311,11312,11313,11314],[11321,11322,11323,11324],[11331,11332,11333,11334]]],\
    [[[12001,12002,12003,12004],[12011,12012,12013,12014],[12021,12022,12023,12024],[12031,12032,12033,12034]],[[12101,12102,12103,12104],[12111,12112,12113,12114],[12121,12122,12123,12124],[12131,12132,12133,12134]],[[12201,12202,12203,12204],[12211,12212,12213,12214],[12212,12222,12223,12224],[12231,12232,12233,12234]],[[12301,12302,12303,12304],[12311,12312,12313,12314],[12321,12322,12323,12324],[12331,12332,12333,12334]]],\
    [[[13001,13002,13003,13004],[13011,13012,13013,13014],[13021,13022,13023,13024],[13031,13032,13033,13034]],[[13101,13102,13103,13104],[13111,13112,13113,13114],[13121,13122,13123,13124],[13131,13132,13133,13134]],[[13201,13202,13203,13204],[13211,13212,13213,13214],[13212,13222,13223,13224],[13231,13232,13233,13234]],[[13301,13302,13303,13304],[13311,13312,13313,13314],[13321,13322,13323,13324],[13331,13332,13333,13334]]]]

l2=[[[[20001,20002,20003,20004],[20011,21002,20013,20014],[20021,20022,20023,20024],[20031,20032,20033,20034]],[[20101,20102,20103,20104],[20111,20112,20113,20114],[20121,20122,20123,20124],[20131,20132,20133,20134]],[[20201,20202,20203,20204],[20211,20212,20213,20214],[20212,20222,20223,20224],[20231,20232,20233,20234]],[[20301,20302,20303,20304],[20311,20312,20313,20314],[20321,20322,20323,20324],[20331,20332,20333,21334]]],\
    [[[21001,21002,21003,21004],[21011,21012,21013,21014],[21021,21022,21023,21024],[21031,21032,21033,21034]],[[21101,21102,21103,21104],[21111,21112,21113,2114],[21121,21122,21123,21124],[21131,21132,21133,21134]],[[21201,21202,21203,21204],[21211,21212,21213,21214],[21212,21222,21223,21224],[21231,21232,21233,21234]],[[21301,21302,21303,21304],[21311,21312,21313,21314],[21321,21322,21323,21324],[21331,21332,21333,21334]]],\
    [[[22001,22002,22003,22004],[22011,22012,22013,22014],[22021,22022,22023,22024],[22031,22032,22033,22034]],[[22101,22102,22103,22104],[22111,22112,22113,22114],[22121,22122,22123,22124],[22131,22132,22133,22134]],[[22201,22202,22203,22204],[22211,22212,22213,22214],[22212,22222,22223,22224],[22231,22232,22233,22234]],[[22301,22302,22303,22304],[22311,22312,22313,22314],[22321,22322,22323,22324],[22331,22332,22333,22334]]],\
    [[[23001,23002,23003,23004],[23011,23012,23013,23014],[23021,23022,23023,23024],[23031,23032,23033,23034]],[[23101,23102,23103,23104],[23111,23112,23113,23114],[23121,23122,23123,23124],[23131,23132,23133,23134]],[[23201,23202,23203,23204],[23211,23212,23213,23214],[23212,23222,23223,23224],[23231,23232,23233,23234]],[[23301,23302,23303,23304],[23311,23312,23313,23314],[23321,23322,23323,23324],[23331,23332,23333,23334]]]]

l3=[[[[30001,30002,30003,30004],[30011,31002,30013,30014],[30021,30022,30023,30024],[30031,30032,30033,30034]],[[30101,30102,30103,30104],[30111,30112,30113,30114],[30121,30122,30123,30124],[30131,30132,30133,30134]],[[30201,30202,30203,30204],[30211,30212,30213,30214],[30212,30222,30223,30224],[30231,30232,30233,30234]],[[30301,30302,30303,30304],[30311,30312,30313,30314],[30321,30322,30323,30324],[30331,30332,30333,31334]]],\
    [[[31001,31002,31003,31004],[31011,31012,31013,31014],[31021,31022,31023,31024],[31031,31032,31033,31034]],[[31101,31102,31103,31104],[31111,31112,31113,31114],[31121,31122,31123,31124],[31131,31132,31133,31134]],[[31201,31202,31203,31204],[31211,31212,31213,31214],[31212,31222,31223,31224],[31231,31232,31233,31234]],[[31301,31302,31303,31304],[31311,31312,31313,31314],[31321,31322,31323,31324],[31331,31332,31333,31334]]],\
    [[[32001,32002,32003,32004],[32011,32012,32013,32014],[32021,32022,32023,32024],[32031,32032,32033,32034]],[[32101,32102,32103,32104],[32111,32112,32113,32114],[32121,32122,32123,32124],[32131,32132,32133,32134]],[[32201,32202,32203,32204],[32211,32212,32213,32214],[32212,32222,32223,32224],[32231,32232,32233,32234]],[[32301,32302,32303,32304],[32311,32312,32313,32314],[32321,32322,32323,32324],[32331,32332,32333,32334]]],\
    [[[33001,33002,33003,33004],[33011,33012,33013,33014],[33021,33022,33023,33024],[33031,33032,33033,33034]],[[33101,33102,33103,33104],[33111,33112,33113,33114],[33121,33122,33123,33124],[33131,33132,33133,33134]],[[33201,33202,33203,33204],[33211,33212,33213,33214],[33212,33222,33223,33224],[33231,33232,33233,33234]],[[33301,33302,33303,33304],[33311,33312,33313,33314],[33321,33322,33323,33324],[33331,33332,33333,33334]]]]
1
l4=[l,l1,l2,l3]

xdarray=np.array(l4)
print("xdarray = ")
print(xdarray)
print(type(xdarray))
print(np.shape(xdarray))
print("\n\nEnter the index to find a number ")
print("index of the number will be equall to the once digit of number -1\n\n\n")
a=int(input("Enter a number in 0-3: " ))
b=int(input("Enter a number in 0-3: " ))
c=int(input("Enter a number in 0-3: " ))
d=int(input("Enter a number in 0-3: " ))
e=int(input("Enter a number in 0-3: " ))
print(xdarray[a][b][c][d][e])
"""Output 
xdarray = 
[[[[[    1     2     3     4]
    [   11    12    13    14]
    [   21    22    23    24]
    [   31    32    33    34]]

   [[  101   102   103   104]
    [  111   112   113   114]
    [  121   122   123   124]
    [  131   132   133   134]]

   [[  201   202   203   204]
    [  211   212   213   214]
    [  212   222   223   224]
    [  231   232   233   234]]

   [[  301   302   303   304]
    [  311   312   313   314]
    [  321   322   323   324]
    [  331   332   333   334]]]


  [[[ 1001  1002  1003  1004]
    [ 1011  1012  1013  1014]
    [ 1021  1022  1023  1024]
    [ 1031  1032  1033  1034]]

   [[ 1101  1102  1103  1104]
    [ 1111  1112  1113  1114]
    [ 1121  1122  1123  1124]
    [ 1131  1132  1133   134]]

   [[ 1201  1202  1203  1204]
    [ 1211  1212  1213  1214]
    [ 1212  1222  1223  1224]
    [ 1231  1232  1233  1234]]

   [[ 1301  1302  1303  1304]
    [ 1311  1312  1313  1314]
    [ 1321  1322  1323  1324]
    [ 1331  1332  1333  1334]]]


  [[[ 2001  2002  2003  2004]
    [ 2011  2012  2013  2014]
    [ 2021  2022  2023  2024]
    [ 2031  2032  2033  2034]]

   [[ 2101  2102  2103  2104]
    [ 2111  2112  2113   114]
    [ 2121  2122  2123  2124]
    [ 2131  2132  2133  2134]]

   [[ 2201  2202  2203  2204]
    [ 2211  2212  2213  2214]
    [ 2212  2222  2223  2224]
    [ 2231  2232  2233  2234]]

   [[ 2301  2302  2303  2304]
    [ 2311  2312  2313  2314]
    [ 2321  2322  2323  2324]
    [ 2331  2332  2333  2334]]]


  [[[ 3001  3002  3003  3004]
    [ 3011  3012  3013  3014]
    [ 3021  3022  3023  3024]
    [ 3031  3032  3033  3034]]

   [[ 3101  3102  3103  3104]
    [ 3111  3112  3113  3114]
    [ 3121  3122  3123  3124]
    [ 3131  3132  3133  3134]]

   [[ 3201  3202  3203  3204]
    [ 3211  3212  3213  3214]
    [ 3212  3222  3223  3224]
    [ 3231  3232  3233  3234]]

   [[ 3301  3302  3303  3304]
    [ 3311  3312  3313  3314]
    [ 3321  3322  3323  3324]
    [ 3331  3332  3333  3334]]]]



 [[[[10001 10002 10003 10004]
    [10011 11002 10013 10014]
    [10021 10022 10023 10024]
    [10031 10032 10033 10034]]

   [[10101 10102 10103 10104]
    [10111 10112 10113 10114]
    [10121 10122 10123 10124]
    [10131 10132 10133 10134]]

   [[10201 10202 10203 10204]
    [10211 10212 10213 10214]
    [10212 10222 10223 10224]
    [10231 10232 10233 10234]]

   [[10301 10302 10303 10304]
    [10311 10312 10313 10314]
    [10321 10322 10323 10324]
    [10331 10332 10333 10334]]]


  [[[11001 11002 11003 11004]
    [11011 11012 11013 11014]
    [11021 11022 11023 11024]
    [11031 11032 11033 11034]]

   [[11101 11102 11103 11104]
    [11111 11112 11113  11114]
    [11121 11122 11123 11124]
    [11131 11132 11133 11134]]

   [[11201 11202 11203 11204]
    [11211 11212 11213 11214]
    [11212 11222 11223 11224]
    [11231 11232 11233 11234]]

   [[11301 11302 11303 11304]
    [11311 11312 11313 11314]
    [11321 11322 11323 11324]
    [11331 11332 11333 11334]]]


  [[[12001 12002 12003 12004]
    [12011 12012 12013 12014]
    [12021 12022 12023 12024]
    [12031 12032 12033 12034]]

   [[12101 12102 12103 12104]
    [12111 12112 12113 12114]
    [12121 12122 12123 12124]
    [12131 12132 12133 12134]]

   [[12201 12202 12203 12204]
    [12211 12212 12213 12214]
    [12212 12222 12223 12224]
    [12231 12232 12233 12234]]

   [[12301 12302 12303 12304]
    [12311 12312 12313 12314]
    [12321 12322 12323 12324]
    [12331 12332 12333 12334]]]


  [[[13001 13002 13003 13004]
    [13011 13012 13013 13014]
    [13021 13022 13023 13024]
    [13031 13032 13033 13034]]

   [[13101 13102 13103 13104]
    [13111 13112 13113 13114]
    [13121 13122 13123 13124]
    [13131 13132 13133 13134]]

   [[13201 13202 13203 13204]
    [13211 13212 13213 13214]
    [13212 13222 13223 13224]
    [13231 13232 13233 13234]]

   [[13301 13302 13303 13304]
    [13311 13312 13313 13314]
    [13321 13322 13323 13324]
    [13331 13332 13333 13334]]]]



 [[[[20001 20002 20003 20004]
    [20011 21002 20013 20014]
    [20021 20022 20023 20024]
    [20031 20032 20033 20034]]

   [[20101 20102 20103 20104]
    [20111 20112 20113 20114]
    [20121 20122 20123 20124]
    [20131 20132 20133 20134]]

   [[20201 20202 20203 20204]
    [20211 20212 20213 20214]
    [20212 20222 20223 20224]
    [20231 20232 20233 20234]]

   [[20301 20302 20303 20304]
    [20311 20312 20313 20314]
    [20321 20322 20323 20324]
    [20331 20332 20333 21334]]]


  [[[21001 21002 21003 21004]
    [21011 21012 21013 21014]
    [21021 21022 21023 21024]
    [21031 21032 21033 21034]]

   [[21101 21102 21103 21104]
    [21111 21112 21113  21114]
    [21121 21122 21123 21124]
    [21131 21132 21133 21134]]

   [[21201 21202 21203 21204]
    [21211 21212 21213 21214]
    [21212 21222 21223 21224]
    [21231 21232 21233 21234]]

   [[21301 21302 21303 21304]
    [21311 21312 21313 21314]
    [21321 21322 21323 21324]
    [21331 21332 21333 21334]]]


  [[[22001 22002 22003 22004]
    [22011 22012 22013 22014]
    [22021 22022 22023 22024]
    [22031 22032 22033 22034]]

   [[22101 22102 22103 22104]
    [22111 22112 22113 22114]
    [22121 22122 22123 22124]
    [22131 22132 22133 22134]]

   [[22201 22202 22203 22204]
    [22211 22212 22213 22214]
    [22212 22222 22223 22224]
    [22231 22232 22233 22234]]

   [[22301 22302 22303 22304]
    [22311 22312 22313 22314]
    [22321 22322 22323 22324]
    [22331 22332 22333 22334]]]


  [[[23001 23002 23003 23004]
    [23011 23012 23013 23014]
    [23021 23022 23023 23024]
    [23031 23032 23033 23034]]

   [[23101 23102 23103 23104]
    [23111 23112 23113 23114]
    [23121 23122 23123 23124]
    [23131 23132 23133 23134]]

   [[23201 23202 23203 23204]
    [23211 23212 23213 23214]
    [23212 23222 23223 23224]
    [23231 23232 23233 23234]]

   [[23301 23302 23303 23304]
    [23311 23312 23313 23314]
    [23321 23322 23323 23324]
    [23331 23332 23333 23334]]]]



 [[[[30001 30002 30003 30004]
    [30011 31002 30013 30014]
    [30021 30022 30023 30024]
    [30031 30032 30033 30034]]

   [[30101 30102 30103 30104]
    [30111 30112 30113 30114]
    [30121 30122 30123 30124]
    [30131 30132 30133 30134]]

   [[30201 30202 30203 30204]
    [30211 30212 30213 30214]
    [30212 30222 30223 30224]
    [30231 30232 30233 30234]]

   [[30301 30302 30303 30304]
    [30311 30312 30313 30314]
    [30321 30322 30323 30324]
    [30331 30332 30333 31334]]]


  [[[31001 31002 31003 31004]
    [31011 31012 31013 31014]
    [31021 31022 31023 31024]
    [31031 31032 31033 31034]]

   [[31101 31102 31103 31104]
    [31111 31112 31113 31114]
    [31121 31122 31123 31124]
    [31131 31132 31133 31134]]

   [[31201 31202 31203 31204]
    [31211 31212 31213 31214]
    [31212 31222 31223 31224]
    [31231 31232 31233 31234]]

   [[31301 31302 31303 31304]
    [31311 31312 31313 31314]
    [31321 31322 31323 31324]
    [31331 31332 31333 31334]]]


  [[[32001 32002 32003 32004]
    [32011 32012 32013 32014]
    [32021 32022 32023 32024]
    [32031 32032 32033 32034]]

   [[32101 32102 32103 32104]
    [32111 32112 32113 32114]
    [32121 32122 32123 32124]
    [32131 32132 32133 32134]]

   [[32201 32202 32203 32204]
    [32211 32212 32213 32214]
    [32212 32222 32223 32224]
    [32231 32232 32233 32234]]

   [[32301 32302 32303 32304]
    [32311 32312 32313 32314]
    [32321 32322 32323 32324]
    [32331 32332 32333 32334]]]


  [[[33001 33002 33003 33004]
    [33011 33012 33013 33014]
    [33021 33022 33023 33024]
    [33031 33032 33033 33034]]

   [[33101 33102 33103 33104]
    [33111 33112 33113 33114]
    [33121 33122 33123 33124]
    [33131 33132 33133 33134]]

   [[33201 33202 33203 33204]
    [33211 33212 33213 33214]
    [33212 33222 33223 33224]
    [33231 33232 33233 33234]]

   [[33301 33302 33303 33304]
    [33311 33312 33313 33314]
    [33321 33322 33323 33324]
    [33331 33332 33333 33334]]]]]
(4, 4, 4, 4, 4)"""
