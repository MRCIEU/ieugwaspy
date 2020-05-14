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


def test_gwasinfo():
    data = ieugwaspy.gwasinfo(['ieu-a-1239','ebi-a-GCST006867'])
    assert len(data) == 2
    assert len(data[0]) > 0
    assert data[0]["pmid"] == 30038396
    assert data[1]["pmid"] == 30054458


def test_phewas():
    data = ieugwaspy.phewas(["rs53576"])
    assert len(data) > 0
    assert len(data[0]) > 0
    assert 0.0 <= data[0]["p"] <= 1.0


def test_tophits():
    data = ieugwaspy.tophits(["ukb-b-12014"])
    assert len(data) > 0
    assert 0.0 <= data[0]["p"] <= 1.0


def test_associations():
    data = ieugwaspy.associations(variantlist=["rs4363"],id=["ukb-b-12014","met-a-717"],access_token="NULL")
    assert len(data) > 0
    assert 0.0 <= data[0]["p"] <= 1.0