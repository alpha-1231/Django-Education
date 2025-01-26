
class FourYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        if (int(value)):
            return int(value)
        else:
            return 2003
        
    def to_url(self, value):
        return "%04d" %value

