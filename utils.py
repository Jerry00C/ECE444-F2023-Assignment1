class Utils:
    def reversed(num):
        if isinstance(num, int):
            return int(str(num)[::-1])
        else:
            raise TypeError

    def formatter(num: int):
        if isinstance(num, int):
            return bin(num), oct(num)
        else:
            raise TypeError


