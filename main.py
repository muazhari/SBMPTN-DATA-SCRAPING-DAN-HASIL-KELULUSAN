import os
import dataCleaner
import crawlSpiders


def main():
    file = open("raw-hasil-sbmptn-2019.txt", 'r')

    dct = dataCleaner.text(file)

    dct.run()

    dct.df.to_csv('dataKelulusanSBM.csv')

    spidersNFiles = dict(spiderPTN='dataPTN.csv',
                         spiderProdi='dataProdi.csv')

    isFilesAvailable = all(os.path.isfile(file)
                           for file in spidersNFiles.values())

    if not(isFilesAvailable):
        spiders = list(spidersNFiles.keys())
        crawlSpiders._crawl(spiders[0])
        crawlSpiders.run(spiders[1:])


if __name__ == '__main__':
    main()
