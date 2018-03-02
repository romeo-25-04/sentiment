class PolarityDict:
    def __init__(self):
        self.words = dict()

    def from_file(self, path):
        '''
        line format: type=weaksubj len=1 word1=abandoned pos1=adj stemmed1=n priorpolarity=negative
        important: keys 'word1', 'pos1' and 'priorpolarity' must be present in line
        last line is a \\n
        :param path: path to file
        '''
        with open(file=path) as f:
            content = f.read()
            lines = [
                line.split(' ')
                for line in content.split('\n')
            ]
            lines.pop()
            lines = [
                [tuple(item.split('=')) for item in line]
                for line in lines
            ]
            lines = [dict(line) for line in lines]
            self.words = dict((line.get('word1')+'_'+line.get('pos1'), line.get('priorpolarity'))
                              for line in lines)

    def from_str(self, pol_str):
        '''
        :param pol_str: <word_pos>\\t<polarity>
        '''
        key, value = pol_str.split('\t')
        self.words[key] = value
