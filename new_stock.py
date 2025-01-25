def calculate_stock_growth_with_dividends(
    initial_investment,
    annual_dividend_yield,
    dividend_payouts_per_year,
    annual_stock_price_change,
    years_held
):
    # calculate values that remain constant through the calculation
    dividend_yield_per_period = annual_dividend_yield / dividend_payouts_per_year
    period_growth_factor = (1 + annual_stock_price_change) ** (1 / dividend_payouts_per_year)
    
    # start with initial investment (creating a new variable so that the original doesn't change)
    investment_value = initial_investment
    
    # loop through each payout period
    for _ in range(years_held * dividend_payouts_per_year):
        # reinvest dividends and apply stock price growth
        investment_value *= (1 + dividend_yield_per_period) * period_growth_factor

    return investment_value

initial_investment = 10000  # initial investment in SEK
annual_dividend_yield = 0.13  # annual dividend yield
dividend_payouts_per_year = 12  # amount of dividend payouts/year
annual_stock_price_change = 0.05  # annual growth in stock price
years_held = 3  # holding period in years

# calculate final value
final_value = calculate_stock_growth_with_dividends(
    initial_investment,
    annual_dividend_yield,
    dividend_payouts_per_year,
    annual_stock_price_change,
    years_held
)

print(f"Your total value after {years_held} year(s) of holding and reinvesting dividends will be {final_value:.2f} SEK")