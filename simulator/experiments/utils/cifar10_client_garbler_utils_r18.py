import numpy as np

## all latency measurements were averaged over 10 runs using the Delphi codebase ## 


## flops_server * freq_server / (flops_iphone * freq_iphone) = ratio

##################################### OFFLINE SECTION #####################################################
###########################################################################################################
NUM_RELU = 557056
CLIENT_LINEAR_STORAGE = 1111050 # total number of elements of `r_i` and `Mr_i - s_i`
SERVER_LINEAR_STORAGE = 557066  # total number of elements of `s_i`

off_client_compute_keygen     = 0.340    # seconds g2g 
off_client_write_key          = 33180308 # bytes g2g 

off_client_compute_he_encrypt = np.array([0.0418369, 0.354997 , 0.3383019, 0.3286377, 0.3275922, 0.3275876,
                                          0.1526939, 0.1522585, 0.1525678, 0.155606 , 0.076363 , 0.0762982,
                                          0.0777117, 0.077087 , 0.0371607, 0.0400202, 0.0402251,
                                          0.0066041]) # seconds g2g

off_client_write_linear       = np.array([ 4719545, 37756304, 37756304, 37756304, 37756304, 37756304,
                                           18878156, 18878156, 18878156, 18878156,  9439082,  9439082,
                                           9439082,  9439082,  4719545,  4719545,  4719545,  
                                           524401]) # bytes g2g


off_client_compute_he_decrypt = np.array([0.0124552, 0.0132234, 0.0128582, 0.0125757, 0.012674 , 0.024943 ,
                                          0.007588 , 0.0073984, 0.0082848, 0.0123529, 0.0063508, 0.0068233,
                                          0.0063844, 0.0072452, 0.0035628, 0.0035845, 0.0040488,
                                          0.0044749]) #seconds g2g

off_server_write_base_ot      = 4096      # bytes g2g 


off_server_compute_he_eval    = np.array([ 1.6988  , 13.5142  , 13.4495  , 13.4172  , 13.3948  , 26.7558  ,
                                           14.5279  , 14.5311  , 14.5088  , 29.5328  , 15.8275  , 15.8042  ,
                                           15.8131  , 31.7222  , 17.1431  , 17.1464  , 17.1434  , 
                                           0.072263]) # seconds g2g

off_server_write_linear       = np.array([4195152, 4195152, 4195152, 4195152, 4195152, 8390296, 2097580,
                                          2097580, 2097580, 4195152, 1048794, 1048794, 1048794, 2097580,
                                          524401,  524401,  524401,  524401]) # bytes g2g

off_client_compute_garble     = 16.9883    # seconds g2g
off_client_compute_encode     = 4.225      # seconds g2g
off_client_write_garbled_c    = 9510061120 # bytes g2g

###########################################################################################################
###########################################################################################################



##################################### ONLINE SECTION ######################################################
###########################################################################################################

on_client_write_linear   = np.array([27689]) # bytes g2g

on_client_write_ext_ot_send = np.array([88080384., 88080384., 88080384., 88080384., 88080384., 44040192.,
                                        44040192., 44040192., 44040192., 22020096., 22020096., 22020096.,
                                        22020096., 11010048., 11010048., 11010048.,
                                        11010048.]) # bytes g2g

on_server_compute_relu   = np.array([1.1429   , 1.1878   , 1.181    , 1.1807   , 1.1803   , 0.6103458,
                                     0.6153632, 0.6030024, 0.6234064, 0.3059403, 0.3009685, 0.3139908,
                                     0.3034331, 0.1588294, 0.1525446, 0.1507039, 0.1576726,
                                     ]) # bytes g2g

on_server_write_ext_ot_setup = np.array([44040192., 44040192., 44040192., 44040192., 44040192., 22020096.,
                                         22020096., 22020096., 22020096., 11010048., 11010048., 11010048.,
                                         11010048.,  5505024.,  5505024.,  5505024., 
                                         5505024.]) # bytes g2g

on_server_write_relu     = np.array([77594630., 77594630., 77594630., 77594630., 77594630., 38797320.,
                                     38797320., 38797320., 38797320., 19398664., 19398664., 19398664.,
                                     19398664.,  9699336.,  9699336.,  9699336.,  9699336.,
                                     ]) # bytes g2g

on_client_compute_encode = np.array([0.2055503, 0.1706788, 0.1968531, 0.1723436, 0.1859499, 0.0759271,
                                     0.0896848, 0.1194852, 0.1718126, 0.0737705, 0.084308 , 0.0669575,
                                     0.1349204, 0.0526059, 0.0618543, 0.0583957, 0.0703536])

on_server_compute_linear = np.array([6.974460e-02, 2.250360e-02, 2.248630e-02, 2.294280e-02,
                                     2.363540e-02, 2.186260e-02, 1.468770e-02, 1.409840e-02,
                                     1.443580e-02, 1.376610e-02, 1.791630e-02, 1.973550e-02,
                                     2.011300e-02, 2.336360e-02, 3.503520e-02, 2.969980e-02,
                                     4.126050e-02, 8.930190e-05, 3.145137e-04]) # seconds g2g


on_server_write_pred     = 131 # bytes

###########################################################################################################
###########################################################################################################


