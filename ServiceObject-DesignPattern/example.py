class OrderService:
    def __init__(self, order):
        self.order = order

    def process_order(self):
        self.update_inventory()
        self.charge_credit_card()
        self.send_confirmation_email()

    def update_inventory(self):
        # logic to update inventory goes here

    def charge_credit_card(self):
        # logic to charge credit card goes here

    def send_confirmation_email(self):
        # logic to send confirmation email goes here
