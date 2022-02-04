
''' Generated by OTF2 Template Engine '''

import ctypes

from .Config import EnumBase, EnumBitset
from .GeneralDefinitions import UNDEFINED_UINT32

@otf2 for enum in enums|event_enums:
@otf2  if enum is bitset_enum:
class @@enum.type.py_ctype@@(EnumBitset, @@enum.type.py_underlying_ctype@@):
@otf2  else:
class @@enum.type.py_ctype@@(EnumBase, @@enum.type.py_underlying_ctype@@):
@otf2  endif
    pass

@otf2  for entry in enum.entries|py_def_enum_entries:
@@entry.name[5:]@@ = @@enum.type.py_ctype@@._construct(@@entry.value@@, "@@entry.suffix@@")
@otf2  for alias in entry.aliases:
@@alias.name[5:]@@ = @@enum.type.py_ctype@@._construct(@@entry.value@@, "@@alias.suffix@@")
@otf2  endfor
@otf2  endfor
@otf2  if enum is enum_with_terminator:
@@enum.terminator.name[5:]@@ = @@enum.type.py_ctype@@(@@enum.terminator.value@@)
@otf2  endif

@otf2 endfor
class MetricValue(ctypes.Union):
    _fields_ = [
        ("signed_int", ctypes.c_int64),
        ("unsigned_int", ctypes.c_uint64),
        ("floating_point", ctypes.c_double),
    ]

COLLECTIVE_ROOT_NONE = CollectiveRoot._construct(UNDEFINED_UINT32.value, "NONE")
COLLECTIVE_ROOT_SELF = CollectiveRoot._construct(UNDEFINED_UINT32.value - 1, "SELF")
COLLECTIVE_ROOT_THIS_GROUP = CollectiveRoot._construct(UNDEFINED_UINT32.value - 2, "THIS_GROUP")

__all__ = [
    @otf2 for enum in enums|event_enums:
    '@@enum.type.py_ctype@@',
    @otf2 for entry in enum.entries:
    '@@entry.name[5:]@@',
    @otf2 endfor
    @otf2 if enum is enum_with_terminator:
    '@@enum.terminator.name[5:]@@',
    @otf2 endif
    @otf2 endfor
    'MetricValue'
]
