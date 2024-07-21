
"""
This module contains functions for calculating technical indicators such as the Stochastic Oscillator and Relative Strength Index (RSI).
"""

def stochastic_oscillator(data, k_window, d_window):
    """
    Calculate the stochastic oscillator.

    Parameters:
        data: Time series data.
        k_window: Window size for %K calculation.
        d_window: Window size for %D calculation.

    Returns:
        k_values, d_values: Stochastic oscillator %K and %D values.
    """
    low_min = data['Low'].rolling(window=k_window).min()
    high_max = data['High'].rolling(window=k_window).max()
    k = 100 * (data['Close'] - low_min) / (high_max - low_min)
    k = k.clip(0, 100)  # Ensure values are between 0 and 100
    d = k.rolling(window=d_window).mean()
    return k, d

def relative_strength_index(data, window):
    """
    Calculate the Relative Strength Index (RSI).

    Parameters:
        data: Time series data.
        window: Window size for RSI calculation.

    Returns:
        rsi: Relative Strength Index values.
    """
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
