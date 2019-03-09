class Transliterator:
    src_to_tgt_chars_table = {}
    def __init__(self, transliteration_table_fn):
        # transliteration_table_fn e.g. krc_transliteration in the repo
        self.src_to_tgt_chars_table = {}
        with open(transliteration_table_fn, 'r', encoding="utf-8") as table_f:
            for line in table_f:
                translit_pair = line.rstrip().split()
                if len(translit_pair) != 2:
                    continue
                self.src_to_tgt_chars_table[translit_pair[0]] = translit_pair[1]
                
    def transliterate(self, line):
        res = []
        for c in line:
            if c in self.src_to_tgt_chars_table.keys():
                if self.src_to_tgt_chars_table[c] != '0':
                    res.append(self.table[c])
        return ''.join(res)
