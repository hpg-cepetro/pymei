import numpy as np
from ctypes import Structure, BigEndianStructure
from ctypes import c_int, c_short, c_float, c_ushort, c_long, c_char


class SEGYTraceHeader (BigEndianStructure):
    _fields_ = [('tracl', c_int),
                ('tracr', c_int),
                ('fldr', c_int),
                ('tracf', c_int),
                ('ep', c_int),
                ('cdp', c_int),
                ('cdpt', c_int),
                ('trid', c_short),
                ('nvs', c_short),
                ('nhs', c_short),
                ('duse', c_short),
                ('offset', c_int),
                ('gelev', c_int),
                ('selev', c_int),
                ('sdepth', c_int),
                ('gdel', c_int),
                ('sdel', c_int),
                ('swdep', c_int),
                ('gwdep', c_int),
                ('scalel', c_short),
                ('scalco', c_short),
                ('sx', c_int),
                ('sy', c_int),
                ('gx', c_int),
                ('gy', c_int),
                ('counit', c_short),
                ('wevel', c_short),
                ('swevel', c_short),
                ('sut', c_short),
                ('gut', c_short),
                ('sstat', c_short),
                ('gstat', c_short),
                ('tstat', c_short),
                ('laga', c_short),
                ('lagb', c_short),
                ('delrt', c_short),
                ('muts', c_short),
                ('mute', c_short),
                ('ns', c_ushort),
                ('dt', c_ushort),
                ('gain', c_short),
                ('igc', c_short),
                ('igi', c_short),
                ('corr', c_short),
                ('sfs', c_short),
                ('sfe', c_short),
                ('slen', c_short),
                ('styp', c_short),
                ('stas', c_short),
                ('stae', c_short),
                ('tatyp', c_short),
                ('afilf', c_short),
                ('afils', c_short),
                ('nofilf', c_short),
                ('nofils', c_short),
                ('lcf', c_short),
                ('hcf', c_short),
                ('lcs', c_short),
                ('hcs', c_short),
                ('year', c_short),
                ('day', c_short),
                ('hour', c_short),
                ('minute', c_short),
                ('sec', c_short),
                ('timebas', c_short),
                ('trwf', c_short),
                ('grnors', c_short),
                ('grnofr', c_short),
                ('grnlof', c_short),
                ('gaps', c_short),
                ('otrav', c_short),
                ('cdpx', c_int),
                ('cdpy', c_int),
                ('Inline3D', c_int),
                ('Crossline3D', c_int),
                ('ShotPoint', c_int),
                ('ShotPointScalar', c_short),
                ('TraceValueMeasurementUnit', c_short),
                ('TransductionConstantMantissa', c_int),
                ('TransductionConstantPower', c_short),
                ('TransductionUnit', c_short),
                ('TraceIdentifier', c_short),
                ('ScalarTraceHeader', c_short),
                ('SourceType', c_short),
                ('SourceEnergyDirectionMantissa', c_int),
                ('SourceEnergyDirectionExponent', c_short),
                ('SourceMeasurementMantissa', c_int),
                ('SourceMeasurementExponent', c_short),
                ('SourceMeasurementUnit', c_short),
                ('UnassignedLong', c_long)]


class BinaryHeader (BigEndianStructure):
    _fields_ = [('jobid', c_int),
                ('lino', c_int),
                ('reno', c_int),
                ('ntrpt', c_short),
                ('nart', c_short),
                ('hdt', c_ushort),
                ('dto', c_ushort),
                ('hns', c_ushort),
                ('nso', c_ushort),
                ('format', c_short),
                ('fold', c_short),
                ('tsort', c_short),
                ('vscode', c_short),
                ('hsfs', c_short),
                ('hsfe', c_short),
                ('hslen', c_short),
                ('hstyp', c_short),
                ('schn', c_short),
                ('hstas', c_short),
                ('hstae', c_short),
                ('htatyp', c_short),
                ('hcorr', c_short),
                ('bgrcv', c_short),
                ('rcvm', c_short),
                ('mfeet', c_short),
                ('polyt', c_short),
                ('vpol', c_short),
                ('Unsigned340', c_char*340)]


class SUTraceHeader(Structure):
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


class SeimicData(object):
    def __init__(self, stream):
        if type(stream) == str:
            self.stream = open(stream, 'rb')
        else:
            self.stream = stream

    def __iter__(self):
        return self

    def __next__(self):
        t = self.readTrace()
        if t is not None:
            return t
        else:
            raise StopIteration


class SU(SeimicData):
    def __init__(self, stream):
        super(SU, self).__init__(stream)

    def readTrace(self):
        header = SUTraceHeader()
        size = self.stream.readinto(header)
        if size is not None and size > 0:
            tdata = (c_float * header.ns)()
            self.stream.readinto(tdata)
            data = np.ctypeslib.as_array(tdata)
            return Trace(header, data)
        else:
            return None


class SEGY(SeimicData):
    def __init__(self, stream):
        super(SEGY, self).__init__(stream)
        self.read_segy_headers = False
        self.textual_header = None
        self.binary_header = None

    def readTrace(self):
        if not self.read_segy_headers:
            self.textual_header = self.stream.read(3200)
            self.stream.readinto(self.binary_header)


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

    @property
    def mx(self):
        return (self.header.gx + self.header.sx) * 0.5 * self.mult

    @property
    def my(self):
        return (self.header.gy + self.header.sy) * 0.5 * self.mult

    @property
    def hx(self):
        return (self.header.gx - self.header.sx) * 0.5 * self.mult

    @property
    def hy(self):
        return (self.header.gy - self.header.sy) * 0.5 * self.mult

    @property
    def cdp(self):
        return self.header.cdp

    @property
    def ns(self):
        return self.header.ns

    @property
    def dt(self):
        return float(self.header.dt) / 1000000
