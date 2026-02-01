CREATE VIEW financial_kpis AS
SELECT
    year,
    revenue,
    net_profit,
    ROUND((net_profit / revenue) * 100, 2) AS net_profit_margin,
    ROUND((net_profit / total_equity) * 100, 2) AS roe_pct,
    debt_equity_ratio
FROM financials;
