
# Generated by OTF2 Template Engine

import _otf2


class _EnumWrapper(object):
    def __init__(self, prefix, enum_type=None):
        # This is a bit ugly, but IMHO at least less ugly than doing it in __getattr__
        self.__dict__['type'] = enum_type
        for (name, candidate) in _otf2.__dict__.items():
            if (enum_type is None or isinstance(candidate, enum_type)) and name.startswith(prefix):
                short_name = name[len(prefix):]
                self.__dict__[short_name] = candidate

    def __setattr__(self, name, value):
        raise AttributeError("Change of values is not allowed.")


# GeneralDefinitions
Undefined = _EnumWrapper("UNDEFINED_")

__all__ = ["Undefined", "FileMode", "FlushType", "Compression"]

FileMode = _otf2.FileMode
FlushType = _otf2.FlushType
Compression = _otf2.Compression
@otf2 for enum in enums:

@@enum.name@@ = _otf2.@@enum.name@@
__all__.append("@@enum.name@@")
@otf2 endfor
