
''' Generated by OTF2 Template Engine '''

import ctypes

from .Config import EnumBase, EnumBitset

class SystemTreeDomain(EnumBase, ctypes.c_uint8):
    pass

SYSTEM_TREE_DOMAIN_MACHINE = SystemTreeDomain._construct(0, "MACHINE")
SYSTEM_TREE_DOMAIN_SHARED_MEMORY = SystemTreeDomain._construct(1, "SHARED_MEMORY")
SYSTEM_TREE_DOMAIN_NUMA = SystemTreeDomain._construct(2, "NUMA")
SYSTEM_TREE_DOMAIN_SOCKET = SystemTreeDomain._construct(3, "SOCKET")
SYSTEM_TREE_DOMAIN_CACHE = SystemTreeDomain._construct(4, "CACHE")
SYSTEM_TREE_DOMAIN_CORE = SystemTreeDomain._construct(5, "CORE")
SYSTEM_TREE_DOMAIN_PU = SystemTreeDomain._construct(6, "PU")
SYSTEM_TREE_DOMAIN_ACCELERATOR_DEVICE = SystemTreeDomain._construct(7, "ACCELERATOR_DEVICE")
SYSTEM_TREE_DOMAIN_NETWORKING_DEVICE = SystemTreeDomain._construct(8, "NETWORKING_DEVICE")

class LocationGroupType(EnumBase, ctypes.c_uint8):
    pass

LOCATION_GROUP_TYPE_UNKNOWN = LocationGroupType._construct(0, "UNKNOWN")
LOCATION_GROUP_TYPE_PROCESS = LocationGroupType._construct(1, "PROCESS")
LOCATION_GROUP_TYPE_ACCELERATOR = LocationGroupType._construct(2, "ACCELERATOR")

class LocationType(EnumBase, ctypes.c_uint8):
    pass

LOCATION_TYPE_UNKNOWN = LocationType._construct(0, "UNKNOWN")
LOCATION_TYPE_CPU_THREAD = LocationType._construct(1, "CPU_THREAD")
LOCATION_TYPE_ACCELERATOR_STREAM = LocationType._construct(2, "ACCELERATOR_STREAM")
LOCATION_TYPE_GPU = LocationType._construct(2, "GPU")
LOCATION_TYPE_METRIC = LocationType._construct(3, "METRIC")

class RegionRole(EnumBase, ctypes.c_uint8):
    pass

REGION_ROLE_UNKNOWN = RegionRole._construct(0, "UNKNOWN")
REGION_ROLE_FUNCTION = RegionRole._construct(1, "FUNCTION")
REGION_ROLE_WRAPPER = RegionRole._construct(2, "WRAPPER")
REGION_ROLE_LOOP = RegionRole._construct(3, "LOOP")
REGION_ROLE_CODE = RegionRole._construct(4, "CODE")
REGION_ROLE_PARALLEL = RegionRole._construct(5, "PARALLEL")
REGION_ROLE_SECTIONS = RegionRole._construct(6, "SECTIONS")
REGION_ROLE_SECTION = RegionRole._construct(7, "SECTION")
REGION_ROLE_WORKSHARE = RegionRole._construct(8, "WORKSHARE")
REGION_ROLE_SINGLE = RegionRole._construct(9, "SINGLE")
REGION_ROLE_SINGLE_SBLOCK = RegionRole._construct(10, "SINGLE_SBLOCK")
REGION_ROLE_MASTER = RegionRole._construct(11, "MASTER")
REGION_ROLE_CRITICAL = RegionRole._construct(12, "CRITICAL")
REGION_ROLE_CRITICAL_SBLOCK = RegionRole._construct(13, "CRITICAL_SBLOCK")
REGION_ROLE_ATOMIC = RegionRole._construct(14, "ATOMIC")
REGION_ROLE_BARRIER = RegionRole._construct(15, "BARRIER")
REGION_ROLE_IMPLICIT_BARRIER = RegionRole._construct(16, "IMPLICIT_BARRIER")
REGION_ROLE_FLUSH = RegionRole._construct(17, "FLUSH")
REGION_ROLE_ORDERED = RegionRole._construct(18, "ORDERED")
REGION_ROLE_ORDERED_SBLOCK = RegionRole._construct(19, "ORDERED_SBLOCK")
REGION_ROLE_TASK = RegionRole._construct(20, "TASK")
REGION_ROLE_TASK_CREATE = RegionRole._construct(21, "TASK_CREATE")
REGION_ROLE_TASK_WAIT = RegionRole._construct(22, "TASK_WAIT")
REGION_ROLE_COLL_ONE2ALL = RegionRole._construct(23, "COLL_ONE2ALL")
REGION_ROLE_COLL_ALL2ONE = RegionRole._construct(24, "COLL_ALL2ONE")
REGION_ROLE_COLL_ALL2ALL = RegionRole._construct(25, "COLL_ALL2ALL")
REGION_ROLE_COLL_OTHER = RegionRole._construct(26, "COLL_OTHER")
REGION_ROLE_FILE_IO = RegionRole._construct(27, "FILE_IO")
REGION_ROLE_POINT2POINT = RegionRole._construct(28, "POINT2POINT")
REGION_ROLE_RMA = RegionRole._construct(29, "RMA")
REGION_ROLE_DATA_TRANSFER = RegionRole._construct(30, "DATA_TRANSFER")
REGION_ROLE_ARTIFICIAL = RegionRole._construct(31, "ARTIFICIAL")
REGION_ROLE_THREAD_CREATE = RegionRole._construct(32, "THREAD_CREATE")
REGION_ROLE_THREAD_WAIT = RegionRole._construct(33, "THREAD_WAIT")
REGION_ROLE_TASK_UNTIED = RegionRole._construct(34, "TASK_UNTIED")
REGION_ROLE_ALLOCATE = RegionRole._construct(35, "ALLOCATE")
REGION_ROLE_DEALLOCATE = RegionRole._construct(36, "DEALLOCATE")
REGION_ROLE_REALLOCATE = RegionRole._construct(37, "REALLOCATE")
REGION_ROLE_FILE_IO_METADATA = RegionRole._construct(38, "FILE_IO_METADATA")

class RegionFlag(EnumBitset, ctypes.c_uint32):
    pass

REGION_FLAG_NONE = RegionFlag._construct(0, "NONE")
REGION_FLAG_DYNAMIC = RegionFlag._construct(( 1 << 0 ), "DYNAMIC")
REGION_FLAG_PHASE = RegionFlag._construct(( 1 << 1 ), "PHASE")

class GroupType(EnumBase, ctypes.c_uint8):
    pass

GROUP_TYPE_UNKNOWN = GroupType._construct(0, "UNKNOWN")
GROUP_TYPE_LOCATIONS = GroupType._construct(1, "LOCATIONS")
GROUP_TYPE_REGIONS = GroupType._construct(2, "REGIONS")
GROUP_TYPE_METRIC = GroupType._construct(3, "METRIC")
GROUP_TYPE_COMM_LOCATIONS = GroupType._construct(4, "COMM_LOCATIONS")
GROUP_TYPE_COMM_GROUP = GroupType._construct(5, "COMM_GROUP")
GROUP_TYPE_COMM_SELF = GroupType._construct(6, "COMM_SELF")

class GroupFlag(EnumBitset, ctypes.c_uint32):
    pass

GROUP_FLAG_NONE = GroupFlag._construct(0, "NONE")
GROUP_FLAG_GLOBAL_MEMBERS = GroupFlag._construct(( 1 << 0 ), "GLOBAL_MEMBERS")

class Base(EnumBase, ctypes.c_uint8):
    pass

BASE_BINARY = Base._construct(0, "BINARY")
BASE_DECIMAL = Base._construct(1, "DECIMAL")

class MetricOccurrence(EnumBase, ctypes.c_uint8):
    pass

METRIC_SYNCHRONOUS_STRICT = MetricOccurrence._construct(0, "SYNCHRONOUS_STRICT")
METRIC_SYNCHRONOUS = MetricOccurrence._construct(1, "SYNCHRONOUS")
METRIC_ASYNCHRONOUS = MetricOccurrence._construct(2, "ASYNCHRONOUS")

class MetricType(EnumBase, ctypes.c_uint8):
    pass

METRIC_TYPE_OTHER = MetricType._construct(0, "OTHER")
METRIC_TYPE_PAPI = MetricType._construct(1, "PAPI")
METRIC_TYPE_RUSAGE = MetricType._construct(2, "RUSAGE")
METRIC_TYPE_USER = MetricType._construct(3, "USER")

class MetricValueProperty(EnumBase, ctypes.c_uint8):
    pass

METRIC_VALUE_ACCUMULATED = MetricValueProperty._construct(0, "ACCUMULATED")
METRIC_VALUE_ABSOLUTE = MetricValueProperty._construct(1, "ABSOLUTE")
METRIC_VALUE_RELATIVE = MetricValueProperty._construct(2, "RELATIVE")
METRIC_VALUE_MASK = MetricValueProperty(15)

class MetricTiming(EnumBase, ctypes.c_uint8):
    pass

METRIC_TIMING_START = MetricTiming._construct(0, "START")
METRIC_TIMING_POINT = MetricTiming._construct(1 << 4, "POINT")
METRIC_TIMING_LAST = MetricTiming._construct(2 << 4, "LAST")
METRIC_TIMING_NEXT = MetricTiming._construct(3 << 4, "NEXT")
METRIC_TIMING_MASK = MetricTiming(240)

class MetricMode(EnumBase, ctypes.c_uint8):
    pass


class MetricScope(EnumBase, ctypes.c_uint8):
    pass

SCOPE_LOCATION = MetricScope._construct(0, "LOCATION")
SCOPE_LOCATION_GROUP = MetricScope._construct(1, "LOCATION_GROUP")
SCOPE_SYSTEM_TREE_NODE = MetricScope._construct(2, "SYSTEM_TREE_NODE")
SCOPE_GROUP = MetricScope._construct(3, "GROUP")

class RecorderKind(EnumBase, ctypes.c_uint8):
    pass

RECORDER_KIND_UNKNOWN = RecorderKind._construct(0, "UNKNOWN")
RECORDER_KIND_ABSTRACT = RecorderKind._construct(1, "ABSTRACT")
RECORDER_KIND_CPU = RecorderKind._construct(2, "CPU")
RECORDER_KIND_GPU = RecorderKind._construct(3, "GPU")

class ParameterType(EnumBase, ctypes.c_uint8):
    pass

PARAMETER_TYPE_STRING = ParameterType._construct(0, "STRING")
PARAMETER_TYPE_INT64 = ParameterType._construct(1, "INT64")
PARAMETER_TYPE_UINT64 = ParameterType._construct(2, "UINT64")

class CartPeriodicity(EnumBase, ctypes.c_uint8):
    pass

CART_PERIODIC_FALSE = CartPeriodicity._construct(0, "FALSE")
CART_PERIODIC_TRUE = CartPeriodicity._construct(1, "TRUE")

class InterruptGeneratorMode(EnumBase, ctypes.c_uint8):
    pass

INTERRUPT_GENERATOR_MODE_TIME = InterruptGeneratorMode._construct(0, "TIME")
INTERRUPT_GENERATOR_MODE_COUNT = InterruptGeneratorMode._construct(1, "COUNT")

class IoParadigmClass(EnumBase, ctypes.c_uint8):
    pass

IO_PARADIGM_CLASS_SERIAL = IoParadigmClass._construct(0, "SERIAL")
IO_PARADIGM_CLASS_PARALLEL = IoParadigmClass._construct(1, "PARALLEL")

class IoParadigmFlag(EnumBitset, ctypes.c_uint32):
    pass

IO_PARADIGM_FLAG_NONE = IoParadigmFlag._construct(0, "NONE")
IO_PARADIGM_FLAG_OS = IoParadigmFlag._construct((1 << 0), "OS")

class IoParadigmProperty(EnumBase, ctypes.c_uint8):
    pass

IO_PARADIGM_PROPERTY_VERSION = IoParadigmProperty._construct(0, "VERSION")

class IoHandleFlag(EnumBitset, ctypes.c_uint32):
    pass

IO_HANDLE_FLAG_NONE = IoHandleFlag._construct(0, "NONE")
IO_HANDLE_FLAG_PRE_CREATED = IoHandleFlag._construct(( 1 << 0 ), "PRE_CREATED")
IO_HANDLE_FLAG_ALL_PROXY = IoHandleFlag._construct(( 1 << 1 ), "ALL_PROXY")

class IoAccessMode(EnumBase, ctypes.c_uint8):
    pass

IO_ACCESS_MODE_READ_ONLY = IoAccessMode._construct(0, "READ_ONLY")
IO_ACCESS_MODE_WRITE_ONLY = IoAccessMode._construct(1, "WRITE_ONLY")
IO_ACCESS_MODE_READ_WRITE = IoAccessMode._construct(2, "READ_WRITE")
IO_ACCESS_MODE_EXECUTE_ONLY = IoAccessMode._construct(3, "EXECUTE_ONLY")
IO_ACCESS_MODE_SEARCH_ONLY = IoAccessMode._construct(4, "SEARCH_ONLY")

class IoStatusFlag(EnumBitset, ctypes.c_uint32):
    pass

IO_STATUS_FLAG_NONE = IoStatusFlag._construct(0, "NONE")
IO_STATUS_FLAG_CLOSE_ON_EXEC = IoStatusFlag._construct(1 << 0, "CLOSE_ON_EXEC")
IO_STATUS_FLAG_APPEND = IoStatusFlag._construct(1 << 1, "APPEND")
IO_STATUS_FLAG_NON_BLOCKING = IoStatusFlag._construct(1 << 2, "NON_BLOCKING")
IO_STATUS_FLAG_ASYNC = IoStatusFlag._construct(1 << 3, "ASYNC")
IO_STATUS_FLAG_SYNC = IoStatusFlag._construct(1 << 4, "SYNC")
IO_STATUS_FLAG_DATA_SYNC = IoStatusFlag._construct(1 << 5, "DATA_SYNC")
IO_STATUS_FLAG_AVOID_CACHING = IoStatusFlag._construct(1 << 6, "AVOID_CACHING")
IO_STATUS_FLAG_NO_ACCESS_TIME = IoStatusFlag._construct(1 << 7, "NO_ACCESS_TIME")
IO_STATUS_FLAG_DELETE_ON_CLOSE = IoStatusFlag._construct(1 << 8, "DELETE_ON_CLOSE")

class CommFlag(EnumBitset, ctypes.c_uint32):
    pass

COMM_FLAG_NONE = CommFlag._construct(0, "NONE")
COMM_FLAG_CREATE_DESTROY_EVENTS = CommFlag._construct(1 << 0, "CREATE_DESTROY_EVENTS")

class RmaWinFlag(EnumBitset, ctypes.c_uint32):
    pass

RMA_WIN_FLAG_NONE = RmaWinFlag._construct(0, "NONE")
RMA_WIN_FLAG_CREATE_DESTROY_EVENTS = RmaWinFlag._construct(1 << 0, "CREATE_DESTROY_EVENTS")

METRIC_ACCUMULATED_START = MetricMode._construct(METRIC_VALUE_ACCUMULATED.value | METRIC_TIMING_START.value, "ACCUMULATED_START")
METRIC_ACCUMULATED_POINT = MetricMode._construct(METRIC_VALUE_ACCUMULATED.value | METRIC_TIMING_POINT.value, "ACCUMULATED_POINT")
METRIC_ACCUMULATED_LAST  = MetricMode._construct(METRIC_VALUE_ACCUMULATED.value | METRIC_TIMING_LAST.value, "ACCUMULATED_LAST")
METRIC_ACCUMULATED_NEXT  = MetricMode._construct(METRIC_VALUE_ACCUMULATED.value | METRIC_TIMING_NEXT.value, "ACCUMULATED_NEXT")
METRIC_ABSOLUTE_POINT    = MetricMode._construct(METRIC_VALUE_ABSOLUTE.value    | METRIC_TIMING_POINT.value, "ABSOLUTE_POINT")
METRIC_ABSOLUTE_LAST     = MetricMode._construct(METRIC_VALUE_ABSOLUTE.value    | METRIC_TIMING_LAST.value, "ABSOLUTE_LAST")
METRIC_ABSOLUTE_NEXT     = MetricMode._construct(METRIC_VALUE_ABSOLUTE.value    | METRIC_TIMING_NEXT.value, "ABSOLUTE_NEXT")
METRIC_RELATIVE_POINT    = MetricMode._construct(METRIC_VALUE_RELATIVE.value    | METRIC_TIMING_POINT.value, "RELATIVE_POINT")
METRIC_RELATIVE_LAST     = MetricMode._construct(METRIC_VALUE_RELATIVE.value    | METRIC_TIMING_LAST.value, "RELATIVE_LAST")
METRIC_RELATIVE_NEXT     = MetricMode._construct(METRIC_VALUE_RELATIVE.value    | METRIC_TIMING_NEXT.value, "RELATIVE_NEXT")

__all__ = [
    'SystemTreeDomain',
    'SYSTEM_TREE_DOMAIN_MACHINE',
    'SYSTEM_TREE_DOMAIN_SHARED_MEMORY',
    'SYSTEM_TREE_DOMAIN_NUMA',
    'SYSTEM_TREE_DOMAIN_SOCKET',
    'SYSTEM_TREE_DOMAIN_CACHE',
    'SYSTEM_TREE_DOMAIN_CORE',
    'SYSTEM_TREE_DOMAIN_PU',
    'SYSTEM_TREE_DOMAIN_ACCELERATOR_DEVICE',
    'SYSTEM_TREE_DOMAIN_NETWORKING_DEVICE',
    'LocationGroupType',
    'LOCATION_GROUP_TYPE_UNKNOWN',
    'LOCATION_GROUP_TYPE_PROCESS',
    'LOCATION_GROUP_TYPE_ACCELERATOR',
    'LocationType',
    'LOCATION_TYPE_UNKNOWN',
    'LOCATION_TYPE_CPU_THREAD',
    'LOCATION_TYPE_ACCELERATOR_STREAM',
    'LOCATION_TYPE_METRIC',
    'RegionRole',
    'REGION_ROLE_UNKNOWN',
    'REGION_ROLE_FUNCTION',
    'REGION_ROLE_WRAPPER',
    'REGION_ROLE_LOOP',
    'REGION_ROLE_CODE',
    'REGION_ROLE_PARALLEL',
    'REGION_ROLE_SECTIONS',
    'REGION_ROLE_SECTION',
    'REGION_ROLE_WORKSHARE',
    'REGION_ROLE_SINGLE',
    'REGION_ROLE_SINGLE_SBLOCK',
    'REGION_ROLE_MASTER',
    'REGION_ROLE_CRITICAL',
    'REGION_ROLE_CRITICAL_SBLOCK',
    'REGION_ROLE_ATOMIC',
    'REGION_ROLE_BARRIER',
    'REGION_ROLE_IMPLICIT_BARRIER',
    'REGION_ROLE_FLUSH',
    'REGION_ROLE_ORDERED',
    'REGION_ROLE_ORDERED_SBLOCK',
    'REGION_ROLE_TASK',
    'REGION_ROLE_TASK_CREATE',
    'REGION_ROLE_TASK_WAIT',
    'REGION_ROLE_COLL_ONE2ALL',
    'REGION_ROLE_COLL_ALL2ONE',
    'REGION_ROLE_COLL_ALL2ALL',
    'REGION_ROLE_COLL_OTHER',
    'REGION_ROLE_FILE_IO',
    'REGION_ROLE_POINT2POINT',
    'REGION_ROLE_RMA',
    'REGION_ROLE_DATA_TRANSFER',
    'REGION_ROLE_ARTIFICIAL',
    'REGION_ROLE_THREAD_CREATE',
    'REGION_ROLE_THREAD_WAIT',
    'REGION_ROLE_TASK_UNTIED',
    'REGION_ROLE_ALLOCATE',
    'REGION_ROLE_DEALLOCATE',
    'REGION_ROLE_REALLOCATE',
    'REGION_ROLE_FILE_IO_METADATA',
    'RegionFlag',
    'REGION_FLAG_NONE',
    'REGION_FLAG_DYNAMIC',
    'REGION_FLAG_PHASE',
    'GroupType',
    'GROUP_TYPE_UNKNOWN',
    'GROUP_TYPE_LOCATIONS',
    'GROUP_TYPE_REGIONS',
    'GROUP_TYPE_METRIC',
    'GROUP_TYPE_COMM_LOCATIONS',
    'GROUP_TYPE_COMM_GROUP',
    'GROUP_TYPE_COMM_SELF',
    'GroupFlag',
    'GROUP_FLAG_NONE',
    'GROUP_FLAG_GLOBAL_MEMBERS',
    'Base',
    'BASE_BINARY',
    'BASE_DECIMAL',
    'MetricOccurrence',
    'METRIC_SYNCHRONOUS_STRICT',
    'METRIC_SYNCHRONOUS',
    'METRIC_ASYNCHRONOUS',
    'MetricType',
    'METRIC_TYPE_OTHER',
    'METRIC_TYPE_PAPI',
    'METRIC_TYPE_RUSAGE',
    'METRIC_TYPE_USER',
    'MetricValueProperty',
    'METRIC_VALUE_ACCUMULATED',
    'METRIC_VALUE_ABSOLUTE',
    'METRIC_VALUE_RELATIVE',
    'METRIC_VALUE_MASK',
    'MetricTiming',
    'METRIC_TIMING_START',
    'METRIC_TIMING_POINT',
    'METRIC_TIMING_LAST',
    'METRIC_TIMING_NEXT',
    'METRIC_TIMING_MASK',
    'MetricMode',
    'METRIC_ACCUMULATED_START',
    'METRIC_ACCUMULATED_POINT',
    'METRIC_ACCUMULATED_LAST',
    'METRIC_ACCUMULATED_NEXT',
    'METRIC_ABSOLUTE_POINT',
    'METRIC_ABSOLUTE_LAST',
    'METRIC_ABSOLUTE_NEXT',
    'METRIC_RELATIVE_POINT',
    'METRIC_RELATIVE_LAST',
    'METRIC_RELATIVE_NEXT',
    'MetricScope',
    'SCOPE_LOCATION',
    'SCOPE_LOCATION_GROUP',
    'SCOPE_SYSTEM_TREE_NODE',
    'SCOPE_GROUP',
    'RecorderKind',
    'RECORDER_KIND_UNKNOWN',
    'RECORDER_KIND_ABSTRACT',
    'RECORDER_KIND_CPU',
    'RECORDER_KIND_GPU',
    'ParameterType',
    'PARAMETER_TYPE_STRING',
    'PARAMETER_TYPE_INT64',
    'PARAMETER_TYPE_UINT64',
    'CartPeriodicity',
    'CART_PERIODIC_FALSE',
    'CART_PERIODIC_TRUE',
    'InterruptGeneratorMode',
    'INTERRUPT_GENERATOR_MODE_TIME',
    'INTERRUPT_GENERATOR_MODE_COUNT',
    'IoParadigmClass',
    'IO_PARADIGM_CLASS_SERIAL',
    'IO_PARADIGM_CLASS_PARALLEL',
    'IoParadigmFlag',
    'IO_PARADIGM_FLAG_NONE',
    'IO_PARADIGM_FLAG_OS',
    'IoParadigmProperty',
    'IO_PARADIGM_PROPERTY_VERSION',
    'IoHandleFlag',
    'IO_HANDLE_FLAG_NONE',
    'IO_HANDLE_FLAG_PRE_CREATED',
    'IO_HANDLE_FLAG_ALL_PROXY',
    'IoAccessMode',
    'IO_ACCESS_MODE_READ_ONLY',
    'IO_ACCESS_MODE_WRITE_ONLY',
    'IO_ACCESS_MODE_READ_WRITE',
    'IO_ACCESS_MODE_EXECUTE_ONLY',
    'IO_ACCESS_MODE_SEARCH_ONLY',
    'IoStatusFlag',
    'IO_STATUS_FLAG_NONE',
    'IO_STATUS_FLAG_CLOSE_ON_EXEC',
    'IO_STATUS_FLAG_APPEND',
    'IO_STATUS_FLAG_NON_BLOCKING',
    'IO_STATUS_FLAG_ASYNC',
    'IO_STATUS_FLAG_SYNC',
    'IO_STATUS_FLAG_DATA_SYNC',
    'IO_STATUS_FLAG_AVOID_CACHING',
    'IO_STATUS_FLAG_NO_ACCESS_TIME',
    'IO_STATUS_FLAG_DELETE_ON_CLOSE',
    'CommFlag',
    'COMM_FLAG_NONE',
    'COMM_FLAG_CREATE_DESTROY_EVENTS',
    'RmaWinFlag',
    'RMA_WIN_FLAG_NONE',
    'RMA_WIN_FLAG_CREATE_DESTROY_EVENTS',
]
