from collections import defaultdict
import glob
import hashlib
import sqlite3
# import matplotlib.pyplot as plt
import os
import pandas as pd
# from venn import venn

# tmp = pd.read_excel('Clusters.xlsx', sheet_name='Sheet2')
# mapper = dict(zip(tmp.Genome, tmp.Cluster))


class DbCanResult:
    def __init__(self, file, preferred_anot='Diamond', **kwargs):
        self.file = file
        self.md5 = hashlib.md5(open(self.file, 'rb').read()).hexdigest()
        self.preferred_anot = preferred_anot

        for arg, value in kwargs.items():
            setattr(self, arg, value)

        self.df = self.createDf()
        self.assignAttributes()
        self.assignSecondaryAttributes()
        self.assignSummary()

    def createDf(self):
        return pd.read_csv(self.file, delimiter='\t', index_col=0)

    def assignAttributes(self):
        self.Diamond = self.df['DIAMOND'].values.tolist()
        self.Diamond = sorted([x for x in self.Diamond if x != '-'])

        self.HMMER = self.df['HMMER'].values.tolist()
        self.HMMER = [v.split('(')[0] for v in self.HMMER]
        self.HMMER = sorted([x for x in self.HMMER if x != '-'])

        self.Hotpep = self.df['Hotpep'].values.tolist()
        self.Hotpep = [v.split('(')[0] for v in self.Hotpep]
        self.Hotpep = sorted([x for x in self.Hotpep if x != '-'])

    def assignSecondaryAttributes(self):
        tmp_dic = defaultdict(list)
        # for hits in getattr(self, self.preferred_anot):
        for hits in self.Diamond:
            if '+' in hits:
                hits = hits.split('+')
            else:
                hits = [hits]
            for hit in hits:
                if '_' in hit:
                    hit = hit.split('_')[0]
                if hit.startswith('GH'):
                    tmp_dic['GH'].append(hit)
                if hit.startswith('GT'):
                    tmp_dic['GT'].append(hit)
                if hit.startswith('PL'):
                    tmp_dic['PL'].append(hit)
                if hit.startswith('CE'):
                    tmp_dic['CE'].append(hit)
                if hit.startswith('AA'):
                    tmp_dic['AA'].append(hit)
                if hit.startswith('CBM'):
                    tmp_dic['CBM'].append(hit)

        for val in ['AA', 'CBM', 'CE', 'GH', 'GT', 'PL']:
            setattr(self, val, sorted(tmp_dic[val]))

    def assignSummary(self):
        self.Summary = {
            'Diamond': len(self.Diamond),
            'HMMER': len(self.HMMER),
            'Hotpep': len(self.Hotpep),
            'GH': len(self.GH),
            'GT': len(self.GT),
            'PL': len(self.PL),
            'CE': len(self.CE),
            'AA': len(self.AA),
            'CBM': len(self.CBM)
        }

    def search_loci(self, pattern, source='DIAMOND'):
        if isinstance(pattern, str):
            return self.df[self.df[source].str.contains(pattern)].to_dict('records')
        elif isinstance(pattern, list):
            return self.df[self.df[source].isin(pattern)].to_dict('records')


class DbCanResults:
    def __init__(self, metadata_file, project, delimiter='\t', preferred_anot='Diamond'):
        self.metadata_file = metadata_file
        self.project = project
        self.delimiter = delimiter
        self.preferred_anot = preferred_anot
        self.metadata_path = os.path.split(self.metadata_file)[0]

        self.df = self.get_metadata_df()
        self.files_samples = list(
            zip(self.df.faa_file, self.df.dbcan_file, self.df.sample_name))
        self.overview_files = self.df['dbcan_file'].values.tolist()

        self.Results = self.parse_overview_files()

    def get_metadata_df(self):
        if self.delimiter == '\t':
            df = pd.read_csv(self.metadata_file, delimiter='\t')
        elif self.delimiter == ',':
            df = pd.read_csv(self.metadata_file, delimiter=',')
        elif self.delimiter == 'excel':
            df = pd.read_excel(self.metadata_file)
        else:
            raise ValueError(
                'Unrecognized metadata delimiter. Please use: [tab, comma, or excel]')
        cols = df.columns
        assert 'faa_file' in cols, 'Need a column labeled "faa_file" to map results.'
        assert 'dbcan_file' in cols, 'Need a column labeled "dbcan_file" to map results.'
        assert 'sample_name' in cols, 'Need a column labeled "sample" to display results.'
        return df

    def parse_overview_files(self):
        tmp = {}

        for faa, dbcan, sample in self.files_samples:
            print(f'{faa}\t{dbcan}\t{sample}')
            full_path = os.path.join(self.metadata_path, dbcan)

            if not os.path.isfile(full_path):
                raise ValueError(
                    f'File {full_path} from {self.metadata_file} does not exist.')

            vals = self.df[self.df.dbcan_file == dbcan].drop(
                ['faa_file', 'dbcan_file', 'sample_name'], axis=1).to_dict('records')[0]
            vals['project'] = self.project

            result = DbCanResult(full_path, self.preferred_anot, **vals)
            # print(vars(result))
            # print('\n\n')
            dict_ = vars(result)
            for cnt, var in enumerate(dict_):
                print(f'{cnt} {var}:\n{dict_[var]}\n')
            tmp[sample] = result

        return tmp


a = DbCanResults('tests/Results1/metadata.txt', project='Results_1')


# for val in a.Results:
#     obj = a.Results[val]
#     vals = obj.search_loci('GH0')
#     print(f'Searching {val}...\n{vals}\n\n')


def place_in_sqlite3(dbcanresults, db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    # cur.execute("CREATE TABLE samples(md5, file, sample_name, project)")
    cur.execute("""
        INSERT INTO samples VALUES
        ('md5_1', 'myfile.txt', 'myfile', 'Results_1')    
    """)
    con.commit()


# place_in_sqlite3('dbcanresults', 'test.db')
