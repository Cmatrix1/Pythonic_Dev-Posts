
MAJOR = 0
MINOR = 0
REVISION = 1

def gen_class():
    MAJOR = 0
    MINOR = 4
    REVISION = 2
    
    class Language:
        MAJOR = 3
        MINOR = 7
        REVISION = 4

        @classmethod
        def version(cls):
            return '{}.{}.{}'.format(MAJOR, MINOR, REVISION)
        
    return Language

instance = gen_class()
print(instance.version())


# 0.4.2
# 3.7.4
# 0.0.1
# Error