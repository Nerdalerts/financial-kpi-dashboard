SELECT
    year,
    revenue,
    ROUND(
      (revenue - LAG(revenue) OVER (ORDER BY year))
      / LAG(revenue) OVER (ORDER BY year) * 100,
      2
    ) AS revenue_growth_pct
FROM financials
ORDER BY year;


SELECT
    year,
    net_profit,
    ROUND(
      (net_profit - LAG(net_profit) OVER (ORDER BY year))
      / LAG(net_profit) OVER (ORDER BY year) * 100,
      2
    ) AS profit_growth_pct
FROM financials
ORDER BY year;

SELECT
    year,
    ROUND((net_profit / revenue) * 100, 2) AS net_profit_margin
FROM financials
ORDER BY year;


SELECT
    year,
    ROUND((net_profit / total_equity) * 100, 2) AS roe_pct
FROM financials
ORDER BY year;


SELECT
    year,
    debt_equity_ratio
FROM financials
ORDER BY year;
