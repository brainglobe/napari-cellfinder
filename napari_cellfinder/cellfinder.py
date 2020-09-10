"""
This module is an example of a barebones numpy reader plugin for napari.

It implements the ``napari_get_reader`` hook specification, (to create
a reader plugin) but your plugin may choose to implement any of the hook
specifications offered by napari.
see: https://napari.org/docs/plugins/hook_specifications.html

Replace code below accordingly.  For complete documentation see:
https://napari.org/docs/plugins/for_plugin_developers.html
"""
import os
from pathlib import Path
from imlib.cells.cells import Cell
from imlib.IO.cells import cells_xml_to_df
from napari_plugin_engine import napari_hook_implementation



def is_cellfinder_dir(path):
    """Determines whether a path is to a brainreg output directory

    Parameters
    ----------
    path : str
        Path to file.

    Returns
    -------
    function or None
        If the path is a recognized format, return a function that accepts the
        same path or list of paths, and returns a list of layer data tuples.
    """
    path = os.path.abspath(path)
    if os.path.isdir(path):
        filelist = os.listdir(path)
    else:
        return False
    for fname in filelist:
        if fname == "cellfinder.json":
            return True
    return False


@napari_hook_implementation(tryfirst=True)
def napari_get_reader(path):
    """A basic implementation of the napari_get_reader hook specification.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    function or None
        If the path is a recognized format, return a function that accepts the
        same path or list of paths, and returns a list of layer data tuples.
    """

    if isinstance(path, str) and is_cellfinder_dir(path):
        return reader_function


def cells_df_as_np(cells_df, new_order=[2, 1, 0], type_column="type"):
    cells_df = cells_df.drop(columns=[type_column])
    cells = cells_df[cells_df.columns[new_order]]
    cells = cells.to_numpy()
    return cells


def get_cell_arrays(cells_file):
    df = cells_xml_to_df(cells_file)

    non_cells = df[df["type"] == Cell.UNKNOWN]
    cells = df[df["type"] == Cell.CELL]

    cells = cells_df_as_np(cells)
    non_cells = cells_df_as_np(non_cells)
    return cells, non_cells


def reader_function(path, point_size=15, opacity=0.6, symbol="ring"):
    """Take a path or list of paths and return a list of LayerData tuples.

    Readers are expected to return data as a list of tuples, where each tuple
    is (data, [add_kwargs, [layer_type]]), "add_kwargs" and "layer_type" are
    both optional.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    layer_data : list of tuples
        A list of LayerData tuples where each tuple in the list contains
        (data, metadata, layer_type), where data is a numpy array, metadata is
        a dict of keyword arguments for the corresponding viewer.add_* method
        in napari, and layer_type is a lower-case string naming the type of layer.
        Both "meta", and "layer_type" are optional. napari will default to
        layer_type=="image" if not provided
    """

    print("Loading cellfinder directory")
    path = Path(os.path.abspath(path))

    classified_cells_path = path / "points" / "cell_classification.xml"



    # with open(path / "brainreg.json") as json_file:
    #     metadata = json.load(json_file)
    #
    # atlas = BrainGlobeAtlas(metadata["atlas"])
    # metadata["atlas_class"] = atlas

    layers = []

    cells, non_cells = get_cell_arrays(str(classified_cells_path))
    layers.append(
        (
            non_cells,
            {"name": "Non cells",
             "size": point_size,
             "n_dimensional": True,
             "opacity": opacity,
             "symbol": symbol,
             "face_color": "lightskyblue"},
            "points",
        )
    )
    layers.append(
        (
            cells,
            {"name": "Cells",
             "size": point_size,
             "n_dimensional": True,
             "opacity": opacity,
             "symbol": symbol,
             "face_color": "lightgoldenrodyellow"},
            "points",
        )
    )

    return layers
