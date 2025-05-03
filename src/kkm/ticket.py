from dataclasses import dataclass

@dataclass
class Ticket:
    name: str
    purchased_at: str
    client_number: str
    card_number: str
    price: str
    starts_at: str
    expires_at: str
    refund_at: str
    lines_zone_1: str
    lines_zone_2: str
    lines_zone_3: str
