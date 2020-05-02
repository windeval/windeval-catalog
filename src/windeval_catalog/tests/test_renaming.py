import pytest
import xarray as xr

from windeval_catalog.preprocessing import create_rename_dict, enforce_standard_names


def test_rename_dict_has_correct_keys():

    dataset = xr.DataArray([1, 2, 3], name="uwnd", dims=("lat",)).to_dataset()

    rename_dict = create_rename_dict(dataset)

    assert any("uwnd" == k for k in rename_dict.keys())
    assert any("lat" == k for k in rename_dict.keys())
    assert len(rename_dict) == 2


def test_enforce_standard_names():

    dataset = xr.DataArray([1, 2, 3], name="uwnd", dims=("lat",)).to_dataset()

    renamed_ds = enforce_standard_names(dataset)

    assert not any("uwnd" == k for k in renamed_ds.data_vars)
    assert not any("lat" == k for k in renamed_ds.dims)
    assert any("eastward_wind" == k for k in renamed_ds.data_vars)
    assert any("latitude" == k for k in renamed_ds.dims)
