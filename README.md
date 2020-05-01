# Windeval catalogs

Contains a test data catalog for windeval.

## Install

```shell
python -m pip install https://github.com/windeval/windeval_catalog.git
```

## Use

```python
In [1]: import windeval_catalog

In [2]: cat = windeval_catalog.get_catalog()

In [3]: display(list(cat))
['field_1', 'field_2', 'station_1', 'station_2']

In [4]: ds_field_1 = cat["field_1"].read()  # cast to numpy array. Use to_dask() for lazy read.

In [5]: display(ds_field_1.mean("time"))
<xarray.Dataset>
Dimensions:    (latitude: 4, longitude: 4)
Coordinates:
  * longitude  (longitude) float32 349.625 349.875 350.125 350.375
  * latitude   (latitude) float32 -10.375 -10.125 -9.875 -9.625
Data variables:
    uwnd       (latitude, longitude) float32 -7.7321405 -7.6297483 ... -7.184493
    vwnd       (latitude, longitude) float32 4.563706 4.64922 ... 4.8660107
    nobs       (latitude, longitude) float32 1.0 1.0 0.75 0.75 ... 0.75 1.0 1.0

```
