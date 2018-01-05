from __future__ import division
import numpy as np
from ctypes import Structure, BigEndianStructure, pointer
from ctypes import c_int32, c_uint32, c_int16, c_float, c_uint16, c_char, c_double
from codecs import decode


class SEGYTraceHeader (BigEndianStructure):
    _fields_ = [('tracl', c_int32),
                ('tracr', c_int32),
                ('fldr', c_int32),
                ('tracf', c_int32),
                ('ep', c_int32),
                ('cdp', c_int32),
                ('cdpt', c_int32),
                ('trid', c_int16),
                ('nvs', c_int16),
                ('nhs', c_int16),
                ('duse', c_int16),
                ('offset', c_int32),
                ('gelev', c_int32),
                ('selev', c_int32),
                ('sdepth', c_int32),
                ('gdel', c_int32),
                ('sdel', c_int32),
                ('swdep', c_int32),
                ('gwdep', c_int32),
                ('scalel', c_int16),
                ('scalco', c_int16),
                ('sx', c_int32),
                ('sy', c_int32),
                ('gx', c_int32),
                ('gy', c_int32),
                ('counit', c_int16),
                ('wevel', c_int16),
                ('swevel', c_int16),
                ('sut', c_int16),
                ('gut', c_int16),
                ('sstat', c_int16),
                ('gstat', c_int16),
                ('tstat', c_int16),
                ('laga', c_int16),
                ('lagb', c_int16),
                ('delrt', c_int16),
                ('muts', c_int16),
                ('mute', c_int16),
                ('ns', c_uint16),
                ('dt', c_uint16),
                ('gain', c_int16),
                ('igc', c_int16),
                ('igi', c_int16),
                ('corr', c_int16),
                ('sfs', c_int16),
                ('sfe', c_int16),
                ('slen', c_int16),
                ('styp', c_int16),
                ('stas', c_int16),
                ('stae', c_int16),
                ('tatyp', c_int16),
                ('afilf', c_int16),
                ('afils', c_int16),
                ('nofilf', c_int16),
                ('nofils', c_int16),
                ('lcf', c_int16),
                ('hcf', c_int16),
                ('lcs', c_int16),
                ('hcs', c_int16),
                ('year', c_int16),
                ('day', c_int16),
                ('hour', c_int16),
                ('minute', c_int16),
                ('sec', c_int16),
                ('timebas', c_int16),
                ('trwf', c_int16),
                ('grnors', c_int16),
                ('grnofr', c_int16),
                ('grnlof', c_int16),
                ('gaps', c_int16),
                ('otrav', c_int16),
                ('cdpx', c_int32),
                ('cdpy', c_int32),
                ('iline', c_int32),
                ('xline', c_int32),
                ('unass', c_char*44)]

    def __eq__(self, other):
        for fld in self._fields_:
            if getattr(self, fld[0]) != getattr(other, fld[0]):
                return False
        return True

    def __ne__(self, other):
        for fld in self._fields_:
            if getattr(self, fld[0]) != getattr(other, fld[0]):
                return True
        return False


class SEGYLGATraceHeader (BigEndianStructure):
    _fields_ = [('tracl',    c_int32),
                ('tracr',    c_int32),
                ('fldr',     c_int32),
                ('tracf',    c_int32),
                ('ep',       c_int32),
                ('cdp',      c_int32),
                ('cdpt',     c_int32),
                ('trid',     c_int16),
                ('nvs',      c_int16),
                ('nhs',      c_int16),
                ('duse',     c_int16),
                ('offset',   c_int32),
                ('gelev',    c_int32),
                ('selev',    c_int32),
                ('sdepth',   c_int32),
                ('gdel',     c_int32),
                ('sdel',     c_int32),
                ('prfAFont', c_int32),
                ('profRecp', c_int32),
                ('scalel',   c_int16),
                ('scalco',   c_int16),
                ('sx',       c_int32),
                ('sy',       c_int32),
                ('gx',       c_int32),
                ('gy',       c_int32),
                ('uniCoor',  c_int16),
                ('velWth',   c_int16),
                ('velSWth',  c_int16),
                ('upholeF',  c_int16),
                ('upholeR',  c_int16),
                ('cEstatF',  c_int16),
                ('cEstatR',  c_int16),
                ('estatApl', c_int16),
                ('timeBkA',  c_int16),
                ('timeBkB',  c_int16),
                ('tmpPrAmt', c_int16),
                ('tmpInMut', c_int16),
                ('tmpFiMut', c_int16),
                ('ns',       c_int16),
                ('dt',       c_int16),
                ('tipoGan',  c_int16),
                ('ganCnstI', c_int16),
                ('ganInicI', c_int16),
                ('fltrcorr', c_int16),
                ('fIniSw',   c_int16),
                ('fFinSw',   c_int16),
                ('compSw',   c_int16),
                ('tipoSw',   c_int16),
                ('tmpIniSw', c_int16),
                ('tmpFinSw', c_int16),
                ('tipoRamp', c_int16),
                ('freqFlt',  c_int16),
                ('slopFlt',  c_int16),
                ('frqfltn',  c_int16),
                ('frqSlpN',  c_int16),
                ('frqBaixa', c_int16),
                ('frqAlta',  c_int16),
                ('slpCBaix', c_int16),
                ('slpCAlta', c_int16),
                ('ano',      c_int16),
                ('dia',      c_int16),
                ('hora',     c_int16),
                ('minuto',   c_int16),
                ('segundos', c_int16),
                ('tipData',  c_int16),
                ('fatTrc',   c_int16),
                ('nEstPos1', c_int16),
                ('nEstTrcI', c_int16),
                ('nEstTrcF', c_int16),
                ('gapSize',  c_int16),
                ('dirLine',  c_int16),
                ('cdpx',     c_float),
                ('cdpy',     c_float),
                ('elevCmp',  c_int32),
                ('iline',    c_int32),
                ('xline',    c_int32),
                ('pick',     c_int32),
                ('estRecp',  c_int32),
                ('estFont',  c_int32),
                ('lineRecp', c_int32),
                ('lineFont', c_int32),
                ('cdfDatum', c_int32),
                ('nrTiroF',  c_float),
                ('byte229',  c_float),
                ('byte233',  c_int32),
                ('byte237',  c_float)]


class SEGYBRTraceHeader (BigEndianStructure):
    _fields_ = [('tracl',    c_int32),
                ('tracr',    c_int32),
                ('fldr',     c_int32),
                ('tracf',    c_int32),
                ('ep',       c_int32),
                ('cdp',      c_int32),
                ('cdpt',     c_int32),
                ('trid',     c_int16),
                ('nvs',      c_int16),
                ('nhs',      c_int16),
                ('duse',     c_int16),
                ('offset',   c_int32),
                ('gelev',    c_int32),
                ('selev',    c_int32),
                ('sdepth',   c_int32),
                ('gdel',     c_int32),
                ('sdel',     c_int32),
                ('prfAFont', c_int32),
                ('profRecp', c_int32),
                ('scalel',   c_int16),
                ('scalco',   c_int16),
                ('sx',       c_int32),
                ('sy',       c_int32),
                ('gx',       c_int32),
                ('gy',       c_int32),
                ('uniCoor',  c_int16),
                ('velWth',   c_int16),
                ('velSWth',  c_int16),
                ('upholeF',  c_int16),
                ('upholeR',  c_int16),
                ('cEstatF',  c_int16),
                ('cEstatR',  c_int16),
                ('estatApl', c_int16),
                ('timeBkA',  c_int16),
                ('timeBkB',  c_int16),
                ('tmpPrAmt', c_int16),
                ('tmpInMut', c_int16),
                ('tmpFiMut', c_int16),
                ('ns',       c_int16),
                ('dt',       c_int16),
                ('tipoGan',  c_int16),
                ('ganCnstI', c_int16),
                ('ganInicI', c_int16),
                ('fltrcorr', c_int16),
                ('fIniSw',   c_int16),
                ('fFinSw',   c_int16),
                ('compSw',   c_int16),
                ('tipoSw',   c_int16),
                ('tmpIniSw', c_int16),
                ('tmpFinSw', c_int16),
                ('tipoRamp', c_int16),
                ('freqFlt',  c_int16),
                ('slopFlt',  c_int16),
                ('frqfltn',  c_int16),
                ('frqSlpN',  c_int16),
                ('frqBaixa', c_int16),
                ('frqAlta',  c_int16),
                ('slpCBaix', c_int16),
                ('slpCAlta', c_int16),
                ('ano',      c_int16),
                ('dia',      c_int16),
                ('hora',     c_int16),
                ('minuto',   c_int16),
                ('segundos', c_int16),
                ('tipData',  c_int16),
                ('fatTrc',   c_int16),
                ('nEstPos1', c_int16),
                ('nEstTrcI', c_int16),
                ('nEstTrcF', c_int16),
                ('gapSize',  c_int16),
                ('dirLine',  c_int16),
                ('cdpx',     c_int32),
                ('cdpy',     c_int32),
                ('elevCmp',  c_int32),
                ('iline',    c_int32),
                ('xline',    c_int32),
                ('pick',     c_int32),
                ('estRecp',  c_int32),
                ('estFont',  c_int32),
                ('lineRecp', c_int32),
                ('lineFont', c_int32),
                ('cdfDatum', c_int32),
                ('nrTiroF',  c_float),
                ('byte229',  c_float),
                ('byte233',  c_int32),
                ('byte237',  c_float)]


class SEGYBinaryHeader (BigEndianStructure):
    _fields_ = [('jobid', c_int32),
                ('lino', c_int32),
                ('reno', c_int32),
                ('ntrpt', c_int16),
                ('nart', c_int16),
                ('hdt', c_uint16),
                ('dto', c_uint16),
                ('hns', c_uint16),
                ('nso', c_uint16),
                ('format', c_int16),
                ('fold', c_int16),
                ('tsort', c_int16),
                ('vscode', c_int16),
                ('hsfs', c_int16),
                ('hsfe', c_int16),
                ('hslen', c_int16),
                ('hstyp', c_int16),
                ('schn', c_int16),
                ('hstas', c_int16),
                ('hstae', c_int16),
                ('htatyp', c_int16),
                ('hcorr', c_int16),
                ('bgrcv', c_int16),
                ('rcvm', c_int16),
                ('mfeet', c_int16),
                ('polyt', c_int16),
                ('vpol', c_int16),
                ('unass', c_char*340)]

    def __eq__(self, other):
        for fld in self._fields_:
            if getattr(self, fld[0]) != getattr(other, fld[0]):
                return False
        return True

    def __ne__(self, other):
        for fld in self._fields_:
            if getattr(self, fld[0]) != getattr(other, fld[0]):
                return True
        return False


class SUTraceHeader(Structure):
    _fields_ = [('tracl', c_int32),
                ('tracr', c_int32),
                ('fldr', c_int32),
                ('tracf', c_int32),
                ('ep', c_int32),
                ('cdp', c_int32),
                ('cdpt', c_int32),
                ('trid', c_int16),
                ('nvs', c_int16),
                ('nhs', c_int16),
                ('duse', c_int16),
                ('offset', c_int32),
                ('gelev', c_int32),
                ('selev', c_int32),
                ('sdepth', c_int32),
                ('gdel', c_int32),
                ('sdel', c_int32),
                ('swdep', c_int32),
                ('gwdep', c_int32),
                ('scalel', c_int16),
                ('scalco', c_int16),
                ('sx', c_int32),
                ('sy', c_int32),
                ('gx', c_int32),
                ('gy', c_int32),
                ('counit', c_int16),
                ('wevel', c_int16),
                ('swevel', c_int16),
                ('sut', c_int16),
                ('gut', c_int16),
                ('sstat', c_int16),
                ('gstat', c_int16),
                ('tstat', c_int16),
                ('laga', c_int16),
                ('lagb', c_int16),
                ('delrt', c_int16),
                ('muts', c_int16),
                ('mute', c_int16),
                ('ns', c_uint16),
                ('dt', c_uint16),
                ('gain', c_int16),
                ('igc', c_int16),
                ('igi', c_int16),
                ('corr', c_int16),
                ('sfs', c_int16),
                ('sfe', c_int16),
                ('slen', c_int16),
                ('styp', c_int16),
                ('stas', c_int16),
                ('stae', c_int16),
                ('tatyp', c_int16),
                ('afilf', c_int16),
                ('afils', c_int16),
                ('nofilf', c_int16),
                ('nofils', c_int16),
                ('lcf', c_int16),
                ('hcf', c_int16),
                ('lcs', c_int16),
                ('hcs', c_int16),
                ('year', c_int16),
                ('day', c_int16),
                ('hour', c_int16),
                ('minute', c_int16),
                ('sec', c_int16),
                ('timbas', c_int16),
                ('trwf', c_int16),
                ('grnors', c_int16),
                ('grnofr', c_int16),
                ('grnlof', c_int16),
                ('gaps', c_int16),
                ('otrav', c_int16),
                ('d1', c_float),
                ('f1', c_float),
                ('d2', c_float),
                ('f2', c_float),
                ('ungpow', c_float),
                ('unscale', c_float),
                ('ntr', c_int32),
                ('mark', c_int16),
                ('shortpad', c_int16),
                ('unass', c_int16 * 14)]

    def __eq__(self, other):
        for fld in self._fields_:
            if getattr(self, fld[0]) != getattr(other, fld[0]):
                return False
        return True

    def __ne__(self, other):
        for fld in self._fields_:
            if getattr(self, fld[0]) != getattr(other, fld[0]):
                return True
        return False


class SeimicData(object):
    def __init__(self, stream, mode='rb'):
        if type(stream) == str:
            if not 'b' in mode:
                mode += 'b'
            self.stream = open(stream, mode)
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

    def next(self):
        t = self.readTrace()
        if t is not None:
            return t
        else:
            raise StopIteration


class SU(SeimicData):
    def __init__(self, stream, mode='rb'):
        super(SU, self).__init__(stream, mode)
        self.fof = 0

    def info(self):
        return ""

    def rewind(self):
        self.fof = 0
        self.stream.seek(self.fof)

    def readTrace(self, fof=-1):
        if fof >= 0:
            self.stream.seek(fof)
        header = SUTraceHeader()
        size = self.stream.readinto(header)
        if size is not None and size > 0:
            tdata = (c_float * header.ns)()
            self.stream.readinto(tdata)
            data = np.ctypeslib.as_array(tdata)
            fof = self.fof
            self.fof += size + header.ns * 4
            return Trace(header, data, fof)
        else:
            return None

    def writeTrace(self, tr):
        self.stream.write(tr.header)
        tr.data.tofile(self.stream)


class SEGY(SeimicData):
    def __init__(self, stream, hdr=SEGYTraceHeader):
        super(SEGY, self).__init__(stream)
        s = decode(self.stream.read(3200), 'cp500')
        v = [s[i:i+80] for i in range(0, len(s), 80)]
        self.textual_header = "\n".join(v)
        self.binary_header = SEGYBinaryHeader()
        self.stream.readinto(self.binary_header)
        self.fof = 3200 + 400
        self.hdr = hdr

    def info(self):
        return self.textual_header

    def rewind(self):
        self.fof = 3200 + 400
        self.stream.seek(self.fof)

    def readTrace(self, fof=-1):
        if fof >= 0:
            self.stream.seek(fof)
        if self.binary_header.format == 1:
            return self.readTraceIBMFloat()
        elif self.binary_header.format == 2:
            raise Exception('4-byte, two\'s complement integer not implemented')
        elif self.binary_header.format == 3:
            raise Exception('2-byte, two\'s complement integer not implemented')
        elif self.binary_header.format == 4:
            raise Exception('4-byte fixed-point with gain not implemented')
        elif self.binary_header.format == 5:
            return self.readTraceIEEEFloat()
        elif self.binary_header.format == 8:
            raise Exception('1-byte, two\'s complement integer not implemented')
        else:
            raise Exception('Unknown data format "%s"' % str(self.binary_header.format))
    
    def readTraceIEEEFloat(self):
        header = self.hdr()
        size = self.stream.readinto(header)
        if size is not None and size > 0:
            tdata = (c_float * header.ns)()
            self.stream.readinto(tdata)
            data = np.ctypeslib.as_array(tdata)
            fof = self.fof
            self.fof += size + header.ns * 4
            return Trace(header, data, fof)
        else:
            return None

    def readTraceIBMFloat(self):
        header = self.hdr()
        size = self.stream.readinto(header)
        if size is not None and size > 0:
            tdata = (c_uint32 * header.ns)()
            self.stream.readinto(tdata)
            s = np.bitwise_and(tdata, 0x80) >> 7
            b1 = np.bitwise_and(tdata, 0x7F)
            b2 = np.bitwise_and(tdata, 0xFF00) >> 8
            b3 = np.bitwise_and(tdata, 0xFF0000) >> 16
            b4 = np.bitwise_and(tdata, 0xFF000000) >> 24
            tdata = (1-2*s.astype(c_double)) * (
                     (b2.astype(c_double) + (
                      b3.astype(c_double) + 
                      b4.astype(c_double) / 2**8) / 2**8) * 
                    16**(b1.astype(c_double)-64-2) )
            data = np.ctypeslib.as_array(tdata)
            fof = self.fof
            self.fof += size + header.ns * 4
            return Trace(header, data, fof)
        else:
            return None


def load(path):
    if path.endswith("su"):
        return SU(path)
    else:
        return SEGY(path)


class Trace(object):
    def __init__(self, header, data, fof):
        self.header = header
        self.data = data
        self.fof = fof
        if header.scalco > 0:
            self.mult = header.scalco
        elif header.scalco < 0:
            self.mult = -1 / header.scalco
        else:
            self.mult = 1

    def copy(self):
        header2 = type(self.header)()
        pointer(header2)[0] = self.header
        return Trace(header2, np.copy(self.data), self.fof)

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
