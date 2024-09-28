import tidypolars as tp
from tidypolars import contains, starts_with, ends_with
import pandas as pd

df = pd.read_csv('data.csv')

tpdf = tp.from_pandas(df)
#tpdf = tp.Tibble(tpdf)

(
    tpdf
    .select(contains('reas'))
)

