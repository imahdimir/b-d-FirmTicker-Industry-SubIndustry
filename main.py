"""

    """

from githubdata import GithubData
from mirutil.df_utils import save_df_as_a_nice_xl as sxl
from mirutil.utils import print_list_as_dict_fmt


class GDUrl :
    cur = 'https://github.com/imahdimir/u-d-FirmTicker-Industry-SubIndustry'
    src = 'https://github.com/imahdimir/d-TSETMC_ID-Shenase'
    trg = 'https://github.com/imahdimir/d-FirmTicker-Industry-SubIndustry'
    ftref = 'https://github.com/imahdimir/d-FirmTickers'

gdu = GDUrl()

class ColName :
    indu = 'گروه صنعت'
    indu_c = 'کد گروه صنعت'
    sub_indu = 'زیر گروه صنعت'
    sub_indu_c = 'کد زیر گروه صنعت'
    tid = 'TSETMC_ID'
    obsd = 'ObsDate'
    ftic = 'FirmTicker'

c = ColName()

def main() :
    pass

    ##

    gd_src = GithubData(gdu.src)
    gd_src.overwriting_clone()
    ##
    ds = gd_src.read_data()
    ##
    print_list_as_dict_fmt(ds.columns)
    ##
    ds = ds[[c.ftic , c.obsd , c.indu , c.indu_c , c.sub_indu , c.sub_indu_c]]
    ds = ds.drop_duplicates()
    ##
    no_dup_ch = {
            c.ftic       : None ,
            c.obsd       : None ,
            c.indu       : None ,
            c.indu_c     : None ,
            c.sub_indu   : None ,
            c.sub_indu_c : None ,
            }

    msk = ds.duplicated(subset = no_dup_ch.keys() , keep = False)
    df1 = ds[msk]

    assert df1.empty , 'There are duplicated rows in the source data!'

    ##

    gd_ref = GithubData(gdu.ftref)
    gd_ref.overwriting_clone()
    ##
    dr = gd_ref.read_data()
    ##
    msk = ~ dr[c.ftic].isin(ds[c.ftic])
    df1 = dr[msk]

    assert df1.empty , 'There are new firm tickers in the reference data!'

    ##

    gd_trg = GithubData(gdu.trg)
    gd_trg.overwriting_clone()

    ##
    dftp = gd_trg.data_fp
    sxl(ds , dftp)
    ##

    msg = 'builded by: '
    msg += gdu.cur
    ##

    gd_trg.commit_and_push(msg)

    ##


    gd_trg.rmdir()
    gd_src.rmdir()
    gd_ref.rmdir()


    ##

##
if __name__ == "__main__" :
    main()

##
# noinspection PyUnreachableCode
if False :
    pass

    ##
    fp = '/Users/mahdi/Dropbox/GitHub/md-Ticker-2-FirmTicker/data.csv'
    df = pd.read_csv(fp)
    ##
    df.iat[0 , 0] = df1.loc[1859 , c.tic]

    ##
    df.to_csv(fp , index = False)

    ##
    ds.drop(columns = c.obsd , inplace = True)

    ##
    ds = ds.sort_values(by = [c.indu_c , c.sub_indu_c])

    ##
    sxl(ds , 'FirmTicker-Industry-SubIndustry.xlsx')


    ##


    ##

##
