from netty_snmp import DispatchSnmpFactory, consts


def test_dispatch():
    factory = DispatchSnmpFactory(
        prefix="192.168.1.0/24",
        port=161,
        version=consts.SnmpVersion.v2c,
        community="public",
        snmp_max_repetitions=20,
        max_workers=16,
    )

    result = factory.dispatch()
    assert result

    result1 = factory.dispatch(discovery_items=["hostname"])

    assert result1

    result2 = factory.dispatch(discovery_items=["hostname", "uptime"])
    assert result2
