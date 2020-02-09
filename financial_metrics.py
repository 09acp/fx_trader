# Week 4
import pandas as pd
import numpy as np
from numpy import array
from numpy import hstack
from matplotlib import pyplot as plt
eps = np.finfo(float).eps # machine accuracy


"""
ALL METRICS IN ONE FUNCTION
"""
def stats(mode,returns,actions): #, path_financial_metrics):
    """Generate statistics report for strategy.

    Parameters
    ----------
    prices: pandas.DataFrame
        Prices of asset universe.
    returns: pandas.Series
        Realised returns of strategy.
    weights: pandas.DataFrame
        Portfolio weights of strategy.

    Returns
    -------
    table: pd.Series
        Strategy report.
    """
    if mode == 1:
        report = {
            'Mean Returns ($)': mean_returns(returns),
            'Cummulative Profit ($)': cum_returns(returns).iloc[-1],
            'Volatility (std $)': std_returns(returns),
            'Sharpe Ratio': sharpe_ratio(returns),
            'Max Drawdown ($)': max_drawdown(returns).iloc[-1],
            'Average Drawdown Time': average_drawdown_time(returns).days,
            'Skewness': skewness(returns),
            'Kurtosis': kurtosis(returns),
            'Tail Ratio': tail_ratio(returns),
            'Value at Risk ($)': value_at_risk(returns),
            'Conditional Value at Risk ($)': conditional_value_at_risk(returns),
            'Hit Ratio (%)': hit_ratio(returns),
            'Average Win to Average Loss': awal(returns),
            'Average Profitability Per Trade ($)': appt(returns),
            'Trader Actions': dict(actions.value_counts())
        }
    else:
        report = {
            'Mean Returns ($)': mean_returns(returns),
            'Cumulative Profit ($)': cum_returns(returns).iloc[-1],
            'Volatility (std $)': std_returns(returns),
            'Sharpe Ratio': sharpe_ratio(returns),
            'Max Drawdown (%)': max_drawdown(returns).iloc[-1],
            'Average Drawdown Time': average_drawdown_time(returns).days,
            'Skewness': skewness(returns),
            'Kurtosis': kurtosis(returns),
            'Tail Ratio': tail_ratio(returns),
            'Value at Risk ($)': value_at_risk(returns),
            'Conditional Value at Risk ($)': conditional_value_at_risk(returns),
            'Hit Ratio (%)': hit_ratio(returns),
            'Average Win to Average Loss': awal(returns),
            'Average Profitability Per Trade ($)': appt(returns)
        }      
    table = pd.Series(
        report,
        name= 'ATVI_log_returns', #(returns.name or 'Strategy'),
        dtype=object
    )
    return table


########################
def hit_ratio(returns):
    """Computes Hit Ratio from simple returns,
    represented by number of positive trades
    over total number of trades.

    Parameters
    ----------
    returns : np.ndarray | pd.Series | pd.DataFrame
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    hit_ratio : float | np.ndarray | pd.Series
        Hit ratio.
    """
    if returns.ndim > 2:
        raise ValueError('returns tensor cannot be handled')
    return np.sum(returns > 0, axis=0) / len(returns)


def cum_returns(returns):
    """
    Computes cumulative profit of trader
    """
    return np.round(returns.cumsum(axis=0))


def pnl(returns):
    """Computes profit and loss (PnL) from simple returns.

    Parameters
    ----------
    returns : np.ndarray | pd.Series | pd.DataFrame
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    pnl : np.ndarray | pd.Series | pd.DataFrame
        Profit and loss.
    """
    if returns.ndim > 2:
        raise ValueError('returns tensor cannot be handled')
    out = returns.copy()
    out = np.add(out, 1)
    out = out.cumprod(axis=0)
    return out



def sharpe_ratio(returns):

    """Computes Sharpe Ratio from simple returns.

    Parameters
    ----------
    returns : np.ndarray | pd.Series | pd.DataFrame
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    sharpe_ratio : float | np.ndarray | pd.Series
        Sharpe ratio.
    """



    if returns.ndim > 2:
        raise ValueError('returns tensor cannot be handled')
    return np.sqrt(len(returns)) * \
        np.mean(returns, axis=0) / (np.std(returns, axis=0) + eps)


def awal(returns):
    """Computes Average Win to Average Loss ratio.

    Parameters
    ----------
    returns : np.ndarray | pd.Series | pd.DataFrame
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    awal : float | np.ndarray | pd.Series
        Average win to average loss ratio.
    """
    if returns.ndim > 2:
        raise ValueError('returns tensor cannot be handled')
    aw = returns[returns > 0].mean(axis=0)
    al = returns[returns < 0].mean(axis=0)
    return np.abs((aw+eps)/(al+eps))


def appt(returns):
    """Computes Average Profitability Per Trade.

    Parameters
    ----------
    returns : np.ndarray | pd.Series | pd.DataFrame
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    appt : float | np.ndarray | pd.Series
        Average profitability per trade.
    """
    if returns.ndim > 2:
        raise ValueError('returns tensor cannot be handled')
    pw = np.sum(returns > 0, axis=0) / len(returns)
    pl = np.sum(returns < 0, axis=0) / len(returns)
    aw = returns[returns > 0].mean(axis=0)
    al = returns[returns < 0].mean(axis=0)
    return pw * aw - pl * al


def value_at_risk(returns, cutoff=0.05):
    """Compute Value at risk (VaR) of a returns stream.

    Parameters
    ----------
    returns : pandas.Series
        Returns of the strategy as a percentage, noncumulative.
    cutoff : float, optional
        Decimal representing the percentage cutoff for the bottom percentile of returns.

    Returns
    -------
    VaR : float
        The VaR value.
    """
    return np.percentile(returns, 100 * cutoff)

##################################################
def drawdown(returns):
    """Computes Drawdown given simple returns.

    Parameters
    ----------
    returns : pandas.Series
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    drawdown : pandas.Series
        Drawdown of strategy.
    """
    profit = cum_returns(returns)
    expanding_max = profit.expanding(1).max()
    drawdown = expanding_max - profit
    return drawdown

def max_drawdown(returns):
    """Computes Max Drawdown given simple returns.

    Parameters
    ----------
    returns : pandas.Series
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    max_drawdown : pandas.Series
        Max drawdown of strategy.
    """
    _drawdown = drawdown(returns)
    return _drawdown.expanding(1).max()


def tail_ratio(returns):
    """Compute tail ratio of returns given simple returns.

    Parameters
    ----------
    returns : pandas.Series
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    tail_ratio : float
        Tail ratio of returns of strategy.
    """
    return np.abs(np.percentile(returns, 95)) / \
        np.abs(np.percentile(returns, 5))

def kurtosis(returns):
    """Compute kurtosis of returns given simple returns.

    Parameters
    ----------
    returns : pandas.Series
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    kurt_returns : float
        Skewness of returns of strategy.
    """
    return returns.kurt(axis=0)

def skewness(returns):
    """Compute skewness of returns given simple returns.

    Parameters
    ----------
    returns : pandas.Series
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    skew_returns : float
        Skewness of returns of strategy.
    """
    return returns.skew(axis=0)

def std_returns(returns):
    """Compute standard deviation of returns given simple returns.

    Parameters
    ----------
    returns : pandas.Series
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    std_returns : float
        Standard deviation of returns of strategy.
    """
    return returns.std(axis=0)

def average_drawdown_time(returns):
    """Computes Average Drawdown Time given simple returns.

    Parameters
    ----------
    returns : pandas.Series
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    average_drawdown_time : datetime.timedelta
        Average drawdown time of strategy.
    """
    _drawdown = drawdown(returns)
    return _drawdown[_drawdown == 0].index.to_series().diff().mean()


def mean_returns(returns):
    """Compute mean returns given simple returns.

    Parameters
    ----------
    returns : pandas.Series
        Returns of the strategy as a percentage, noncumulative.

    Returns
    -------
    mean_returns : float
        Mean returns of strategy.
    """
    return returns.mean(axis=0)

def conditional_value_at_risk(returns, cutoff=0.05):
    """Compute Conditional value at risk (CVaR) of a returns stream.
    CVaR measures the expected single-day returns of an asset on that asset's
    worst performing days, where "worst-performing" is defined as falling below
    ``cutoff`` as a percentile of all daily returns.

    Parameters
    ----------
    returns : pandas.Series
        Returns of the strategy as a percentage, noncumulative.
    cutoff : float, optional
        Decimal representing the percentage cutoff for the bottom percentile of returns.

    Returns
    -------
    CVaR : float
        The CVaR value.
    """
    cutoff_index = int((len(returns) - 1) * cutoff)
    return np.mean(np.partition(returns, cutoff_index)[:cutoff_index + 1])
