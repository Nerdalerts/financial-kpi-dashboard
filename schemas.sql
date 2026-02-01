create table financials(
year INT primary key,
revenue numeric not null,
net_profit numeric,
total_assets numeric,
total_equity numeric,
total_debt numeric,
debt_equity_ratio numeric,
company_name text,
currency text,
source text
);
