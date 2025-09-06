class Money:

    _exchange_rates = {
        'USD: {'AMD' : 400, 'EUR': 1/1.08},
        'AMD: {'USD': 1/400},
        'EUR': {'USD': 1.08}

    }

    def __init__(self, amount, currency):
        """
        Initializes a Money object.
        :param amount: The amount of money (float or int).
        :param currency: The type of currency (string, e.g., 'USD', 'AMD', 'EUR').
        """
        self.amount = float(amount)
        self.currency = currency.upper()

    def __repr__(self):
        """
        Returns a string representation of the object.
        """
        return f"{self.amount:,.2f} {self.currency}"

    def exchange(self, new_currency):
        """
        Exchanges the money to another currency.
        :param new_currency: The new currency for the exchange.
        :return: A new Money object with the new currency.
        """
        new_currency = new_currency.upper()
        if new_currency == self.currency:
            return Money(self.amount, self.currency)
        except KeyError:
            # Rate not found, try to use an intermediate currency (e.g., USD)
            if 'USD' in self._exchange_rates[self.currency] and new_currency in self._exchange_rates['USD']:
                usd_amount = self.exchange('USD').amount
                rate = self._exchange_rates['USD'][new_currency]
                new_amount = usd_amount * rate
                return Money(new_amount, new_currency)
            else:
                raise ValueError(f"Exchange rate from {self.currency} to {new_currency} was not found.")

    def __add__(self, other):
        """
        Adds two Money objects together.
        """
        if self.currency == other.currency:
            new_amount = self.amount + other.amount
            return Money(new_amount, self.currency)
        else:
            # Convert the second object to the first's currency and add
            converted_amount = other.exchange(self.currency).amount
            new_amount = self.amount + converted_amount
            return Money(new_amount, self.currency)
        def __sub__(self, other):
        """
        Subtracts two Money objects.
        """
        if self.currency == other.currency:
            new_amount = self.amount - other.amount
            return Money(new_amount, self.currency)
        else:
            # Convert the second object to the first's currency and subtract
            converted_amount = other.exchange(self.currency).amount
            new_amount = self.amount - converted_amount
            return Money(new_amount, self.currency)

    def __truediv__(self, other):
        """
        Divides a Money object by another Money object or a number.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Cannot divide by zero.")
            new_amount = self.amount / other
            return Money(new_amount, self.currency)
        elif isinstance(other, Money):
            # Divides two Money objects. The result is a number.
            converted_amount = other.exchange(self.currency).amount
            if converted_amount == 0:
                raise ValueError("Cannot divide by zero.")
            return self.amount / converted_amount
        else:
            raise TypeError("Division is only possible with a number or a Money object.")

    def __mul__(self, other):
        """
        Multiplies a Money object by a number.
        """
        if isinstance(other, (int, float)):
            new_amount = self.amount * other
            return Money(new_amount, self.currency)
        else:
            raise TypeError("Multiplication is only possible with a number.")

    def __rmul__(self, other):
        """
        Multiplies by a number if the number comes first.
        """
        return self.__mul__(other)
    
    def __eq__(self, other):
        """
        Checks the equality of two Money objects.
        """
        if self.currency == other.currency:
            return self.amount == other.amount
        else:
            return self.amount == other.exchange(self.currency).amount
        if __name__ == "__main__":
    # Create Money objects
    usd_money = Money(100, 'USD')
    amd_money = Money(20000, 'AMD')
    eur_money = Money(50, 'EUR')

    print(f"Created objects:")
    print(f"USD amount: {usd_money}")
    print(f"AMD amount: {amd_money}")
    print(f"EUR amount: {eur_money}\n")

    print("--- Exchanging ---")
    usd_to_amd = usd_money.exchange('AMD')
    print(f"{usd_money} exchanged to AMD is: {usd_to_amd}")
    eur_to_usd = eur_money.exchange('USD')
    print(f"{eur_money} exchanged to USD is: {eur_to_usd}\n")

    print("--- Addition ---")
    sum_result = usd_money + amd_money
    print(f"{usd_money} + {amd_money} = {sum_result}")

    print("--- Subtraction ---")
    sub_result = usd_to_amd - amd_money
    print(f"{usd_to_amd} - {amd_money} = {sub_result}\n")

    print("--- Multiplication ---")
    mul_result = usd_money * 2
    print(f"{usd_money} * 2 = {mul_result}\n")

    print("--- Equality Check ---")
    equal_result = Money(100, 'USD') == Money(40000, 'AMD')
    print(f"{Money(100, 'USD')} == {Money(40000, 'AMD')} ? {equal_result}")
    
    unequal_result = Money(100, 'USD') == Money(30000, 'AMD')
    print(f"{Money(100, 'USD')} == {Money(30000, 'AMD')} ? {unequal_result}")
