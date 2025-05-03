from kkm import ticket

def test_initialize():
    t = ticket.Ticket('name', 'purchased_at', 'client_number', 'card_number', 'price', 'starts_at', 'expires_at', 'refund_at', 'lines_zone1', 'lines_zone2', 'lines_zone3')

    assert t.name == 'name'
    assert t.purchased_at == 'purchased_at'
    assert t.client_number == 'client_number'
    assert t.card_number == 'card_number'
    assert t.price == 'price'
    assert t.starts_at == 'starts_at'
    assert t.expires_at == 'expires_at'
    assert t.refund_at == 'refund_at'
    assert t.lines_zone_1 == 'lines_zone1'
    assert t.lines_zone_2 == 'lines_zone2'
    assert t.lines_zone_3 == 'lines_zone3'
