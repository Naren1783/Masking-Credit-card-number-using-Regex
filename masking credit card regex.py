import re

def mask_credit_card(card_number):
     masked_number = re.sub(r'(\d{4})$', r'XXXX', card_number)
     return masked_number

card1 = "1234567890123456"
card2 = "1111-2222-3333-4444"

print(f"Original: {card1}, Masked: {mask_credit_card(card1)}")
print(f"Original: {card2}, Masked: {mask_credit_card(card2)}")

