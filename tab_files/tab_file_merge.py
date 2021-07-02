import os
from pathlib import Path
import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent

GO_COLNAMES = [
    'location', 'info', 'sublocation', 'relation', 'function', 'go_code', 'number', 'letters', 
    'more_text', 'more_letters', 'none', 'publication', 'date'
]

def tab_file_merge(genes_filename, go_filename):
    df_genes = pd.read_csv(genes_filename, sep = '\t', names = ['gene', 'sublocation'])
    df_go = pd.read_csv(go_filename, sep = '\t', names = GO_COLNAMES)

    df_go = df_go.loc[df_go['info'].notnull()]

    reduced_go = df_go[['sublocation', 'go_code']].drop_duplicates()
    reduced_go.sort_values(['sublocation', 'go_code'], inplace = True)

    loc_to_go = reduced_go.groupby('sublocation', as_index = False).agg({
        'go_code' : lambda x : ','.join(x)
    })

    df = df_genes.merge(loc_to_go, 'left', on = 'sublocation')

    return

def main():
    genes_file = os.path.join(SCRIPT_DIR, 'BLASTX_GENES.csv')
    go_file = os.path.join(SCRIPT_DIR, 'ATH_GO_GOSLIM.csv')

    x = tab_file_merge(genes_file, go_file)
    return

if __name__ == '__main__':
    main()