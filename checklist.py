import yaml, os, sys
from pprint import pprint
from data_fetcher import get_financials
from utils.ratios import (
    revenue_cagr, roic, free_cash_flow_pos,
    debt_equity, payout_ratio
)

cfg_path = os.path.join(os.path.dirname(__file__), "config.yml")
with open(cfg_path, "r", encoding="utf-8") as f:
    CFG = yaml.safe_load(f)

def evaluate(ticker):
    fin = get_financials(ticker)
    return {
        "CAGR": revenue_cagr(fin) >= CFG["min_cagr"],
        "ROIC": roic(fin) >= CFG["min_roic"],
        "FCF+": free_cash_flow_pos(fin),
        "Debt": debt_equity(fin) <= CFG["max_de_ratio"],
        "Moat": True,  # mock
        "Payout": payout_ratio(fin) <= CFG["max_payout"],
        "Pass#": sum([
            revenue_cagr(fin) >= CFG["min_cagr"],
            roic(fin) >= CFG["min_roic"],
            free_cash_flow_pos(fin),
            debt_equity(fin) <= CFG["max_de_ratio"],
            True,
            payout_ratio(fin) <= CFG["max_payout"]
        ])
    }

if __name__ == "__main__":
    tk = sys.argv[1]
    pprint(evaluate(tk.upper()))