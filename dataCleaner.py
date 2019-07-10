import pandas as pd


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def excludeStr(strList, strToExclude):
    return any(str not in strToExclude for str in strList)


class text:
    def __init__(self, file):
        self.data = {
            'nomor_peserta': [],
            'nama': [],
            'kode_prodi': []
        }

        self.df = pd.DataFrame(self.data)

        self.raw_file = file
        self.raw_lines = self.raw_file.readlines()

    def updateDataframe(self):
        self.df = pd.DataFrame(self.data)

    def tabling(self, i):
        stripped_line = self.raw_lines[i].strip()
        splitted_line = stripped_line.split()

        if len(splitted_line) >= 3 and hasNumbers(splitted_line[0]):

            self.data['nomor_peserta'].append(splitted_line[0])
            self.data['nama'].append(self.clean_label_nama(splitted_line))
            self.data['kode_prodi'].append(splitted_line[-1])

    def clean_label_nama(self, splitted_line):
        label_nama = []
        for n in splitted_line[1:]:
            if not hasNumbers(n):
                label_nama.append(n)

        joined_label_nama = " ".join(label_nama)

        return joined_label_nama

    def run(self):
        for i in range(0, len(self.raw_lines)):
            self.tabling(i)

        self.updateDataframe()
