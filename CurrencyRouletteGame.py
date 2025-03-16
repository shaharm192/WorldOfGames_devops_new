import random
import requests


def get_exchange_rate():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return data["rates"]["ILS"]
    except Exception as e:
        print(f"⚠️ Error fetching exchange rate: {e}")
        return None  # Return None if API fails


def get_money_interval(difficulty, exchange_rate, usd_amount):

    true_value = usd_amount * exchange_rate
    margin = max(1, 6 - difficulty)
    return true_value - margin, true_value + margin


def get_guess_from_user(usd_amount):
    while True:
        try:
            guess = float(input(f"💰 How much is {usd_amount} USD in ILS? (Your Guess): "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")



def play_currency_roulette(difficulty):
    exchange_rate = get_exchange_rate()
    if exchange_rate is None:
        print("❌ Could not retrieve exchange rate. Try again later.")
        return False

    usd_amount = random.randint(1, 100)
    min_value, max_value = get_money_interval(difficulty, exchange_rate, usd_amount)

    print(f"\n💵 USD Amount: {usd_amount} USD")
    print(f"📈 Current exchange rate: {exchange_rate:.2f} ILS per USD")

    user_guess = get_guess_from_user(usd_amount)

    if min_value <= user_guess <= max_value:
        print(f"🎉 Correct! The actual value was {usd_amount * exchange_rate:.2f} ILS.")
        return True
    else:
        print(f"❌ Incorrect! The correct range was {min_value:.2f} - {max_value:.2f} ILS.")
        return False

