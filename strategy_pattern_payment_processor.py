"""
Write a program to implement a Configurable Payment Processing System Using Strategy Pattern.
"""
# Step 1: Define a base PaymentStrategy interface using standard Python class structure
class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement the 'pay' method.")

# Step 2: Implement concrete payment strategies inheriting from PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):
        masked_card = "*" * 12 + str(self.card_number)[-4:]
        print(f"Paid ${amount:.2f} using Credit Card ({masked_card}) for {self.card_holder}.")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal account ({self.email}).")


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Bitcoin wallet ({self.wallet_address[:6]}...{self.wallet_address[-4:]}).")


# Step 3 & 4: Create PaymentProcessor class that uses PaymentStrategy and allows switching strategies at runtime
class PaymentProcessor:
    def __init__(self, strategy=None):
        self._strategy = strategy

    def set_strategy(self, strategy):
        """Allows switching payment strategies dynamically at runtime."""
        self._strategy = strategy

    def process_payment(self, amount):
        if not self._strategy:
            print("Error: No payment strategy set.")
            return
        self._strategy.pay(amount)


# --- Demonstration of Runtime Strategy Switching ---
if __name__ == "__main__":
    # Create concrete payment strategies
    credit_card = CreditCardPayment("1234567890123456", "John Doe")
    paypal = PayPalPayment("john.doe@example.com")
    bitcoin = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

    # Initialize the processor with Credit Card strategy
    processor = PaymentProcessor(credit_card)
    print("--- Transaction 1 ---")
    processor.process_payment(150.00)

    # Switch strategy to PayPal at runtime
    print("\n--- Transaction 2 ---")
    processor.set_strategy(paypal)
    processor.process_payment(75.50)

    # Switch strategy to Bitcoin at runtime
    print("\n--- Transaction 3 ---")
    processor.set_strategy(bitcoin)
    processor.process_payment(300.25)

"""
--> Output
--- Transaction 1 ---
Paid $150.00 using Credit Card (************3456) for John Doe.

--- Transaction 2 ---
Paid $75.50 using PayPal account (john.doe@example.com).

--- Transaction 3 ---
Paid $300.25 using Bitcoin wallet (1A1zP1...vfNa).
"""