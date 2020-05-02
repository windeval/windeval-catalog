standard_names_mapping = {
    "wind_speed": ["WS_401",],
    "eastward_wind": ["WU_422", "uwnd",],
    "northward_wind": ["WV_423", "vwnd",],
    "longitude": ["lon", "long"],
    "latitude": ["lat",],
    "time": ["t",],
}


def create_rename_dict(dataset):
    """Create a rename dict by inverting the standard names mapping.

    Currently, there is _one_ large rename dict containing rules for data vars
    and for dims.
    """
    rename_dict = {}
    for target_name, source_names in standard_names_mapping.items():
        for sn in source_names:
            if (sn in dataset) or (sn in dataset.dims):
                rename_dict[sn] = target_name
                break
    return rename_dict


def enforce_standard_names(dataset):
    """Rename things in an Xarray obj to standard names."""
    rename_dict = create_rename_dict(dataset)
    return dataset.rename(rename_dict)
