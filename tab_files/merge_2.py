import pandas as pd


def main():
    ids = pd.read_csv('GO_ID_DF.csv', header = None, sep = '\t', names = ['go_code', 'value'])

    annotation_colnames = ['col' + str(x) for x in range(15)]
    annotation_colnames[2] = 'sublocation'
    annotation_colnames[5] = 'go_code'

    annotations = pd.read_csv('Annotations.csv', header = None, sep = '\t', names = annotation_colnames)

    g = annotations.groupby(['go_code'], as_index = False).agg({
        'sublocation' : lambda x : ','.join(x)
    })

    ids = ids.merge(g, 'left', on = 'go_code')

    return

if __name__ == '__main__':
    main()