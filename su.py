import numpy as np
from ctypes import Structure, c_int, c_short, c_float, c_ushort


class TraceHeader(Structure):
    _fields_ = [("tracl", c_int),
                ("tracr", c_int),
                ("fldr", c_int),
                ("tracf", c_int),
                ("ep", c_int),
                ("cdp", c_int),
                ("cdpt", c_int),
                ("trid", c_short),
                ("nvs", c_short),
                ("nhs", c_short),
                ("duse", c_short),
                ("offset", c_int),
                ("gelev", c_int),
                ("selev", c_int),
                ("sdepth", c_int),
                ("gdel", c_int),
                ("sdel", c_int),
                ("swdep", c_int),
                ("gwdep", c_int),
                ("scalel", c_short),
                ("scalco", c_short),
                ("sx", c_int),
                ("sy", c_int),
                ("gx", c_int),
                ("gy", c_int),
                ("counit", c_short),
                ("wevel", c_short),
                ("swevel", c_short),
                ("sut", c_short),
                ("gut", c_short),
                ("sstat", c_short),
                ("gstat", c_short),
                ("tstat", c_short),
                ("laga", c_short),
                ("lagb", c_short),
                ("delrt", c_short),
                ("muts", c_short),
                ("mute", c_short),
                ("ns", c_ushort),
                ("dt", c_ushort),
                ("gain", c_short),
                ("igc", c_short),
                ("igi", c_short),
                ("corr", c_short),
                ("sfs", c_short),
                ("sfe", c_short),
                ("slen", c_short),
                ("styp", c_short),
                ("stas", c_short),
                ("stae", c_short),
                ("tatyp", c_short),
                ("afilf", c_short),
                ("afils", c_short),
                ("nofilf", c_short),
                ("nofils", c_short),
                ("lcf", c_short),
                ("hcf", c_short),
                ("lcs", c_short),
                ("hcs", c_short),
                ("year", c_short),
                ("day", c_short),
                ("hour", c_short),
                ("minute", c_short),
                ("sec", c_short),
                ("timbas", c_short),
                ("trwf", c_short),
                ("grnors", c_short),
                ("grnofr", c_short),
                ("grnlof", c_short),
                ("gaps", c_short),
                ("otrav", c_short),
                ("d1", c_float),
                ("f1", c_float),
                ("d2", c_float),
                ("f2", c_float),
                ("ungpow", c_float),
                ("unscale", c_float),
                ("ntr", c_int),
                ("mark", c_short),
                ("shortpad", c_short),
                ("unass", c_short * 14)]


class SU(object):
    def __init__(self, stream):
        if type(stream) == str:
            self.stream = open(stream, 'rb')
        else:
            self.stream = stream

    def readTrace(self):
        header = TraceHeader()
        size = self.stream.readinto(header)
        if size is not None and size > 0:
            tdata = (c_float * header.ns)()
            self.stream.readinto(tdata)
            data = np.ctypeslib.as_array(tdata)
            return Trace(header, data)
        else:
            return None

    def __iter__(self):
        return self

    def __next__(self):
        t = self.readTrace()
        if t is not None:
            return t
        else:
            raise StopIteration


class Trace(object):
    def __init__(self, header, data):
        self.header = header
        self.data = data
        if header.scalco > 0:
            self.mult = header.scalco
        elif header.scalco < 0:
            self.mult = 1 / header.scalco
        else:
            self.mult = 1

    @property
    def gx(self):
        return self.header.gx * self.mult

    @property
    def gy(self):
        return self.header.gy * self.mult

    @property
    def sx(self):
        return self.header.sx * self.mult

    @property
    def sy(self):
        return self.header.sy * self.mult


if __name__ == "__main__":
    d = '/opt/repo-processamento/dados-desenvolvimento/data/'
    sy = []
    gy = []

    for t in SU(d + 'simple-syntetic-micro.su'):
        sy.append(t.sy)
        gy.append(t.gy)

    import matplotlib.pyplot as plt
    plt.scatter(sy, gy)
    plt.show()
