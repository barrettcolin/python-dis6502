import memory

SYMBOLS = {
    0xffe0: 'OSRDCH',
    0xfff4: 'OSBYTE',
}

class Memory(memory.Memory):
    @classmethod
    def from_file(cls, file_, org=None, symbols=None):
        syms = SYMBOLS
        if symbols:
            syms.update(symbols)

        return cls(file_.read(), 0 if org is None else org, syms)
