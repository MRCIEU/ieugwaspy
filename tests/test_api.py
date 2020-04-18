#!/usr/local/bin/python3
import ieugwaspy


def test_apistatus():
    data = ieugwaspy.api_status()
    assert data["API version"]


def test_variantstoid():
    data = ieugwaspy.variants_to_rsid(["10:44865737"])
    assert data[0] == "rs7777"
    assert len(data) == 1


def test_studylookup():
    data = ieugwaspy.gwasinfo(["ieu-a-1239"])
    assert data[0]["trait"] == "Years of schooling"
    alldata = ieugwaspy.gwasinfo()
    assert len(alldata) > 10000
