import polars as pl

gdp = "../data/gdp.csv"
credit_g = "../data/credit_g.csv"
ir = "../data/ir.csv"
m2 = "../data/m2.csv"
real_est_p = "../data/real_est_p.csv"
unemp_r = "../data/unemp_r.csv"

gdp = pl.read_csv(gdp, try_parse_dates=True)
credit_g = pl.read_csv(credit_g, try_parse_dates=True)
ir = pl.read_csv(ir, try_parse_dates=True)
m2 = pl.read_csv(m2, try_parse_dates=True)
real_est_p = pl.read_csv(real_est_p, try_parse_dates=True)
unemp_r = pl.read_csv(unemp_r, try_parse_dates=True)

(
    (gdp.plot.point(x="Year", y="GDP (current US$)"))
    .properties(width=500)
    .configure_scale(zero=False)
)
