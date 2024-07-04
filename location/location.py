class Location(tuple)
    def __new__(cls, latitude, longitude, altitude=None)
        if not (-90 = latitude = 90)
            raise ValueError(Latitude must be between -90 and 90 degrees.)
        if not (-180 = longitude = 180)
            raise ValueError(Longitude must be between -180 and 180 degrees.)
        if altitude is not None and not isinstance(altitude, (int, float))
            raise ValueError(Altitude must be a number.)
        if altitude is None
            return super(Location, cls).__new__(cls, (latitude, longitude))
        else
            return super(Location, cls).__new__(cls, (latitude, longitude, altitude))

    def __repr__(self)
        if len(self) == 3
            return fLocation(latitude={self[0]}, longitude={self[1]}, altitude={self[2]})
        else
            return fLocation(latitude={self[0]}, longitude={self[1]})

    @property
    def latitude(self)
        return self[0]

    @property
    def longitude(self)
        return self[1]

    @property
    def altitude(self)
        return self[2] if len(self) == 3 else None

    def to_tuple(self)
        return tuple(self)
