# Copyright (c) 2011, Gabriele Favalessa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# -*- coding: utf-8 -*-

def hx(x, size=2):
    fmt = '$%%0%dX' % size
    return fmt % x

class M_AC(object):
    def __init__(self, **kwargs):
        pass

    def __eq__(self, other):
        return isinstance(other, M_AC)

    def __repr__(self):
        return "A"

    def __str__(self):
        return ''

class M_XR(object):
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return ''

class M_YR(object):
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return ''

class M_AIND(object):
    def __init__(self, **kwargs):
        pass

class M_FC(object):
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return ''

class M_FD(object):
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return ''

class M_FI(object):
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return ''

class M_FV(object):
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return ''

class M_IMM(object):
    def __init__(self, **kwargs):
        self.immed = kwargs['immed']

    def __repr__(self):
        return '#%s' % hx(self.immed)

class M_INDX(object):
    def __init__(self, **kwargs):
        self.offset = kwargs['offset']

class M_INDY(object):
    def __init__(self, **kwargs):
        self.offset = kwargs['offset']

class M_NONE(object):
    def __init__(self, **kwargs):
        pass

    def __eq__(self, other):
        return isinstance(other, M_NONE)

    def __repr__(self):
        return ''

class M_PC(object):
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return ''

class M_REL(object):
    def __init__(self, **kwargs):
        self.offset = kwargs['offset']

        if self.offset >= 128:
            self.offset -= 256

    def __repr__(self):
        return '.%+d' % self.offset

    def to_string(self, addr, memory):
        addr += self.offset + 2

        try:
            return memory.symbols[addr]
        except KeyError:
            annotations = memory.annotations[addr]
            if 'J' in  annotations or 'T' in annotations:
                return 'L%04X' % addr
            else:
                return hx(addr, 4)

class M_SP(object):
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return ''

class M_SR(object):
    def __init__(self, **kwargs):
        pass

class AddrBase(object):
    def __init__(self, **kwargs):
        self.addr = kwargs['addr']

    def to_string(self, addr, memory):
        try:
            return memory.symbols[self.addr]
        except KeyError:
            annotations = memory.annotations[self.addr]
            if 'J' in  annotations or 'T' in annotations:
                fmt = 'L%%0%dX' % self.size
                return fmt % self.addr
            else:
                return hx(self.addr, self.size)

class M_ABS(AddrBase):
    size = 4

class M_ABSX(AddrBase):
    size = 4

class M_ABSY(AddrBase):
    size = 4

class M_ADDR(AddrBase):
    size = 4
    def __repr__(self):
        return hx(self.addr, 4)

class M_ZERO(AddrBase):
    size = 2
    def __repr__(self):
        return hx(self.addr)

class M_ZERX(AddrBase):
    size = 2
    def __repr__(self):
        return hx(self.addr) + ',X'

    def to_string(self, addr, memory):
        return super(M_ZERX, self).to_string(addr, memory) + ',X'

class M_ZERY(AddrBase):
    size = 2
    def __repr__(self):
        return hx(self.addr) + ',Y'

    def to_string(self, addr, memory):
        return super(M_ZERY, self).to_string(addr, memory) + ',Y'
