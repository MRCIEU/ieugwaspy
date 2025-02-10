

def test_apistatus(ieugwaspy_instance):
    data = ieugwaspy_instance.status()
    assert data["API__VERSION"]


def test_user(ieugwaspy_instance):
    data = ieugwaspy_instance.user()
    assert "uid" in data["user"]


def test_variants_to_rsid(ieugwaspy_instance):
    data = ieugwaspy_instance.variants_to_rsid(["rs1234", "10:44865737"])
    assert set(data) == {"rs1234", "rs7777"}


def test_gwasinfo_single(ieugwaspy_instance):
    data = ieugwaspy_instance.gwasinfo(["ieu-a-1239"])
    assert data[0]["trait"] == "Years of schooling"


def test_gwasinfo_multiple(ieugwaspy_instance):
    data = ieugwaspy_instance.gwasinfo(["ieu-a-1239", "ieu-a-998", "ebi-a-GCST006867"])
    assert len(data) == 2
    assert "ieu-a-998" not in data
    assert all([data[i]["pmid"] in [30038396, 30054458] for i in range(len(data))])


def test_gwasinfo_files_single(ieugwaspy_instance):
    data = ieugwaspy_instance.gwasinfo_files(["ieu-a-1239"])
    assert len(data["ieu-a-1239"]) >= 1


def test_gwasinfo_files_multiple(ieugwaspy_instance):
    data = ieugwaspy_instance.gwasinfo_files(["ieu-a-1239", "ieu-a-998", "ebi-a-GCST006867"])
    assert len(data) == 2
    assert "ieu-a-998" not in data
    assert len(data["ieu-a-1239"]) > 0 and len(data["ebi-a-GCST006867"]) > 0


def test_gwasinfo_all(ieugwaspy_instance):
    alldata = ieugwaspy_instance.gwasinfo()
    assert len(alldata) > 48000


def test_phewas(ieugwaspy_instance):
    data = ieugwaspy_instance.phewas(["rs53576"])
    assert len(data) > 0
    assert len(data[0]) > 0
    assert 0.0 <= data[0]["p"] <= 1.0


def test_tophits(ieugwaspy_instance):
    data = ieugwaspy_instance.tophits(["ukb-b-12014"])
    assert len(data) > 0
    assert 0.0 <= data[0]["p"] <= 1.0


def test_associations(ieugwaspy_instance):
    data = ieugwaspy_instance.associations(variant=["rs4363"], id=["ukb-b-12014", "met-a-717"])
    assert len(data) > 0
    assert 0.0 <= data[0]["p"] <= 1.0
