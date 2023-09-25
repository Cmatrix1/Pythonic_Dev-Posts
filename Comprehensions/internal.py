import dis

compiled_code = compile('[i**2 for i in (1, 2, 3)]', 
                        filename='', mode='eval')

dis.dis(compiled_code)

#  2 LOAD_CONST        0 (<code object <listcomp> at 0x000002107E1C7D20, file "", line 1>)
#  4 MAKE_FUNCTION     0
#  6 LOAD_CONST        1 ((1, 2, 3))
#  8 GET_ITER
# 10 PRECALL           0
# 14 CALL              0
# 24 RETURN_VALUE