from windeval_catalog.cat_handling import get_catalog, set_env_vars

import os


def test_env_vars_are_set():
    set_env_vars()
    assert "WINDEVAL_DATA_DIR" in os.environ


def test_catalog_has_desired_entries():
    set_env_vars()
    cat = get_catalog()
    print(list(cat))

    assert any("field_1" == k for k in list(cat))
    assert any("field_2" == k for k in list(cat))
    assert any("station_1" == k for k in list(cat))
    assert any("station_2" == k for k in list(cat))
