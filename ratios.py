def revenue_cagr(fin):
    rev = fin["revenue"]
    return (rev[-1] / rev[0]) ** (1 / (len(rev) - 1)) - 1

def roic(fin):
    return fin["net_income_latest"] / (fin["total_debt"] + fin["total_equity"])

def free_cash_flow_pos(fin):
    return all(fc > 0 for fc in fin["free_cash_flow"])

def debt_equity(fin):
    return fin["total_debt"] / fin["total_equity"]

def payout_ratio(fin):
    return fin["dividends_paid"] / fin["net_income_latest"]