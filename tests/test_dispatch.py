from netty_snmp import DispatchSnmpFactory, consts


def test_dispatch():
    factory = DispatchSnmpFactory(
        prefix="192.168.1.0/26",
        port=161,
        version=consts.SnmpVersion.v2c,
        community="public",
        snmp_max_repetitions=consts.SNMP_MAX_REPETITIONS,
        max_workers=64,
    )

    result = factory.dispatch()
    assert result

    result1 = factory.dispatch(discovery_items=["hostname"])

    assert result1

    result2 = factory.dispatch(discovery_items=["hostname", "uptime"])
    assert result2
