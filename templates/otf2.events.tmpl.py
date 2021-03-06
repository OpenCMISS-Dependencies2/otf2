# Generated by OTF2 Template Engine

import re
from numbers import Number, Integral
from six import with_metaclass, string_types

from .attribute_list import AttributeList
from .enums import Base, ParameterType


def _replace_doxygen_commands(doc_string):
    if doc_string is not None:
        p = re.compile(r'@eref\{([^}]*)\}')
        doc_string = p.sub(r':py:class:`\1`', doc_string)
        doc_string = doc_string.replace('@b', '')
    return doc_string


class _EventMeta(type):
    def __new__(mcls, name, bases, namespace):
        clazz = type.__new__(mcls, name, bases, namespace)
        old_doc = namespace.get("__doc__")
        clazz.__doc__ = _replace_doxygen_commands(old_doc)
        return clazz


class _Event(with_metaclass(_EventMeta, object)):
    def __init__(self, time, attributes=None):
        self.time = time
        if attributes is not None:
            if not isinstance(attributes, dict):
                raise TypeError("Unexpected type for argument: attributes")
        self.attributes = attributes

    def __str__(self):
        return str(self.__dict__)


def _get_string_ref(writer, value):
    # The writer argument is the event writer, but for get_ref its the definition
    # writer. But we do not want, that this string definition will be written now
    return writer._archive.definitions.strings.get_ref(value, writer=None)
@otf2 for event in events:
@otf2  if event == Metric:

class Metric(_Event):
    """
        This event represents a measurement point.
    """

    _fields = ("time", "int", "the timestamp"), \
              ("metric", "MetricRef", "the :py:class:`otf2.definitions.MetricClass` or \
               :py:class:`otf2.definitions.MetricInstance`"), \
              ("values", "array", "an array of values, one for each :py:class:`otf2.definitions.MetricMember`"), \
              ("attributes", "dict", "a dict with an :py:class:`otf2.definitions.Attribute` \
               referencing a suitable value.")

    def __init__(self, time, metric, values, attributes=None):
        super(Metric, self).__init__(time, attributes)
        self.metric = metric
        if isinstance(values, Number):
            self.values = [values]
        else:
            self.values = values

    @property
    def value(self):
        if len(self.values) != 1:
            raise AttributeError(
                "Trying to access singular metric value on metric event with {} values".format(
                    len(self.values)))
        return self.values[0]

    @value.setter
    def value(self, new_value):
        if len(self.values) != 1:
            raise AttributeError(
                "Trying to access singular metric value on metric event with {} values".format(
                    len(self.values)))
        self.values[0] = new_value

    @property
    def member(self):
        if len(self.values) != 1:
            raise AttributeError(
                "Trying to access singular metric value on metric event with {} values".format(
                    len(self.values)))
        return self.metric.members[0]

    @property
    def scaled_value(self):
        if self.member.base == Base.DECIMAL:
            base = 10
        else:
            base = 2

        return self.value * pow(base, self.member.exponent)

    @property
    def scaled_values(self):
        def get_base(base):
            if base == Base.DECIMAL:
                return 10
            return 2

        return [value * pow(get_base(member.base), member.exponent) for value, member in
                zip(self.values, self.metric.members)]

    @classmethod
    def _construct(cls, registry, time, metric_ref, type_ids, union_values):
        # Type ids is redundant with the ids from the metric itself, we don't check the consistency
        # for performance reaons
        metric = registry.metrics[metric_ref]
        values = metric._convert_unions(union_values)
        return cls(time, metric, values)

    def _write(self, writer):
        with AttributeList(writer._archive.definitions, self.attributes) as al:
            writer._metric(al._handle, self.time, self.metric._ref, self.metric._type_ids,
                           self.metric._convert_values(self.values))
@otf2  elif event == ParameterString:
class ParameterString(_Event):
    """A ParameterString record marks that in the current region, the specified
string parameter has the specified value.

    """
    _fields = ("time", "int", "the timestamp"), \
              ("parameter", "ParameterRef", ""), \
              ("string", "StringRef", ""), \
              ("attributes", "dict", "a dict with an :py:class:`otf2.definitions.Attribute` \
               referencing a suitable value.")

    def __init__(self, time, parameter, string, attributes=None):
        super(ParameterString, self).__init__(time, attributes)
        if parameter.parameter_type != ParameterType.STRING:
            raise TypeError("Expected parameter of type STRING, but got {}".format(parameter.parameter_type))
        self.parameter = parameter
        self.string = string

    @classmethod
    def _construct(cls, registry, time, parameter, string):
        return cls(time, registry.parameters[parameter], registry.strings[string])

    def _write(self, writer):
        with AttributeList(writer._archive.definitions, self.attributes) as al:
            writer._parameter_string(al._handle, self.time, self.parameter._ref, _get_string_ref(writer, self.string))
@otf2  elif event == ProgramBegin:

class ProgramBegin(_Event):
    """The ProgramBegin record marks the begin of the program.

This event is restricted to happen at most once on any @eref{Location}
in a @eref{LocationGroup} that is of type
@eref{OTF2_LOCATION_GROUP_TYPE_PROCESS}.

If there is a ProgramBegin record, a corresponding
@eref{ProgramEnd} record on any @eref{Location} in the same
@eref{LocationGroup} is mandatory and vice versa.

None of the timestamps recorded within the same
@eref{LocationGroup} must be smaller than ProgramBegin's timestamp.

    """
    _fields = ("time", "int", "the timestamp"), \
              ("programName", "StringRef", ""), \
              ("programArguments", "array", "an array of program arguments"), \
              ("attributes", "dict", "a dict with an :py:class:`otf2.definitions.Attribute` \
               referencing a suitable value.")

    def __init__(self, time, program_name, program_arguments, attributes=None):
        super(ProgramBegin, self).__init__(time, attributes)
        self.program_name = program_name
        self.program_arguments = program_arguments

    @classmethod
    def _construct(cls, registry, time, program_name_ref, program_argument_refs):
        return cls(time, registry.strings[program_name_ref], [registry.strings[ref] for ref in program_argument_refs])

    def _write(self, writer):
        with AttributeList(writer._archive.definitions, self.attributes) as al:
            writer._program_begin(al._handle, self.time,
                                  _get_string_ref(writer, self.program_name),
                                  [_get_string_ref(writer, argument) for argument in self.program_arguments])
@otf2  else:

class @@event.name@@(_Event):
    """@@event.doc@@

    """
    _fields = ("time", "int", "the timestamp"), \
              @otf2 for attr in event.attributes:
              ("@@attr.name@@", "@@attr.type.py_ctype@@", ""), \
              @otf2 endfor
              ("attributes", "dict", "a dict with an :py:class:`otf2.definitions.Attribute` \
               referencing a suitable value.")

    def __init__(self, time@@event.py_funcargs(case='lower')@@, attributes=None):
        super(@@event.name@@, self).__init__(time, attributes)
        @otf2 for attr in event.attributes:
        @otf2  if attr.py_parameter_check:
        if @@attr.py_parameter_check[0]@@:
            raise @@attr.py_parameter_check[1]@@
        @otf2  endif
        self.@@attr.lower@@ = @@attr.lower@@
        @otf2 endfor

    @classmethod
    def _construct(cls, registry, time@@event.py_funcargs(case='lower')@@):
        return cls(time@@event.formatargs('{lower}',
                                          format_refs='registry.{def_ref.ref_lower}s[{lower}]')@@)

    def _write(self, writer):
        with AttributeList(writer._archive.definitions, self.attributes) as al:
            writer._@@event.lower@@(al._handle, self.time@@event.formatargs('self.{lower}', format_refs='self.{lower}._ref')@@)
@otf2  endif
@otf2 endfor
