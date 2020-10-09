# napari-cellfinder

[![License](https://img.shields.io/pypi/l/napari-cellfinder.svg?color=green)](https://github.com/napari/napari-cellfinder/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-cellfinder.svg?color=green)](https://pypi.org/project/napari-cellfinder)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-cellfinder.svg?color=green)](https://python.org)
[![tests](https://github.com/adamltyson/napari-cellfinder/workflows/tests/badge.svg)](https://github.com/adamltyson/napari-cellfinder/actions)
[![codecov](https://codecov.io/gh/adamltyson/napari-cellfinder/branch/master/graph/badge.svg)](https://codecov.io/gh/adamltyson/napari-cellfinder)

Visualise cellfinder results with napari


----------------------------------


## Installation

You can install `napari-cellfinder` via [pip]:

    pip install napari-cellfinder

## Usage
* Open napari (however you normally do it, but typically just type `napari` into your terminal)
* Load your raw data (drag and drop the data directories into napari, one at a time)
* Drag and drop your cellfinder output directory into napari.

The plugin will then load your detected cells (in yellow) and the rejected cell 
candidates (in blue). If you carried out registration, then these results will be 
overlaid (similarly to the [napari-brainreg] plugin, but transformed to the 
coordinate space of your raw data).

![load_data](https://raw.githubusercontent.com/brainglobe/napari-cellfinder/master/resources/load_data.gif)
**Loading raw data**

![load_data](https://raw.githubusercontent.com/brainglobe/napari-cellfinder/master/resources/load_results.gif)
**Loading cellfinder results**

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-cellfinder" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari-brainreg]: https://github.com/brainglobe/napari-brainreg
[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/adamltyson/napari-cellfinder/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/