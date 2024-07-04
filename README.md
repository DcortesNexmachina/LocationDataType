# LocationDataType

A custom Python data type for handling geographical coordinates including latitude, longitude, and optional altitude. This data type extends the built-in tuple, making it compatible with most tuple operations and iterable contexts.

## Features

- Represents geographical coordinates with latitude, longitude, and optional altitude.
- Validates the range of latitude and longitude values.
- Inherits from `tuple`, so it is iterable and can be used in contexts expecting a tuple.
- Provides a clear and readable string representation.
- Easily integrates with pandas DataFrames.

## Installation

You can install the package via pip:

```sh
pip install location

