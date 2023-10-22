class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    
    @property
    def version(self):
        return '{}.{}.{}'.format(self.MAJOR, self.MINOR, self.REVISION)
    
    @classmethod
    def cls_version(cls):
        return '{}.{}.{}'.format(cls.MAJOR, cls.MINOR, cls.REVISION)
    
    @staticmethod
    def static_version():
        return '{}.{}.{}'.format(Language.MAJOR, Language.MINOR, Language.REVISION)
