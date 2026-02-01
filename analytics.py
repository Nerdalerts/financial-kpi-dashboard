import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

from urllib.parse import quote_plus
password = quote_plus("IITbomb@y123")

engine = create_engine(
    f"postgresql+psycopg2://postgres:{password}@localhost:5432/finance_db"
)

df = pd.read_sql(
    "SELECT * FROM financials ORDER BY year",
    engine
)
print(df)

years = df.shape[0] - 1
revenue_cagr = (
    (df["revenue"].iloc[-1] / df["revenue"].iloc[0]) ** (1 / years) - 1
) * 100
profit_cagr = (
    (df["net_profit"].iloc[-1] / df["net_profit"].iloc[0]) ** (1 / years) - 1
) * 100

# CAGR CALCULATION
print(f"Revenue CAGR: {revenue_cagr:.2f}%")
print(f"Profit CAGR: {profit_cagr:.2f}%")

# PROFIT VOLATILITY
profit_volatility = df["net_profit"].pct_change().std() * 100
print(f"Profit Volatility: {profit_volatility:.2f}%")

# ROLLING AVERAGES
df["revenue_rolling_avg"] = df["revenue"].rolling(window=2).mean()
df["profit_rolling_avg"] = df["net_profit"].rolling(window=2).mean()
print(df[["year", "revenue_rolling_avg", "profit_rolling_avg"]])


# ROE STABILITY
df["roe_pct"] = (df["net_profit"] / df["total_equity"]) * 100
roe_std = df["roe_pct"].std()
print(f"ROE Stability (Std Dev): {roe_std:.2f}")

# RISK SCORE CALCULATION
df["risk_score"] = (
    df["debt_equity_ratio"] * 0.6 +
    (1 - df["net_profit"].pct_change().fillna(0)) * 0.4
)
print(df[["year", "risk_score"]])

#KPI SUMMARY TABLE (FOR POWER BI / REPORT)
kpi_summary = {
    "Revenue CAGR (%)": round(revenue_cagr, 2),
    "Profit CAGR (%)": round(profit_cagr, 2),
    "Profit Volatility (%)": round(profit_volatility, 2),
    "ROE Stability": round(roe_std, 2)
}
kpi_df = pd.DataFrame.from_dict(kpi_summary, orient="index", columns=["Value"])
print(kpi_df)

