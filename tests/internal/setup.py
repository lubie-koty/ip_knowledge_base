import ipaddress

from app.internal.setup import create_knowledge_base


def test_create_knowledge_base():
    # given
    test_data = [
        {"tag": "foo", "ip_network": "192.0.2.0/24"},
        {"tag": "bar", "ip_network": "192.0.2.8/29"},
        {"tag": "bar", "ip_network": "10.20.0.0/16"},
        {"tag": "SPAM", "ip_network": "10.20.30.40/32"},
    ]
    test_values = [
        ("192.0.2.7", ["foo"]),
        ("192.0.2.9", ["bar", "foo"]),
        ("10.20.30.40", ["SPAM", "bar"]),
        ("10.20.30.41", ["bar"]),
        ("10.20.130.40", ["bar"]),
        ("10.120.30.40", []),
        ("0.0.0.0", []),
        ("192.0.3.9", []),
        ("203.0.113.187", []),
        ("255.255.255.255", []),
    ]

    # when
    knowledge_base = create_knowledge_base(test_data)

    # then
    for test_value, expected_result in test_values:
        query_result = set()
        for tags in knowledge_base.at(int(ipaddress.ip_address(test_value))):
            query_result |= tags.data
        assert sorted(query_result) == expected_result
