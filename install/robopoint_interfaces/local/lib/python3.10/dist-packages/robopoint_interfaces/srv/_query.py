# generated from rosidl_generator_py/resource/_idl.py.em
# with input from robopoint_interfaces:srv/Query.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Query_Request(type):
    """Metaclass of message 'Query_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('robopoint_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'robopoint_interfaces.srv.Query_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__query__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__query__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__query__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__query__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__query__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Query_Request(metaclass=Metaclass_Query_Request):
    """Message class 'Query_Request'."""

    __slots__ = [
        '_query',
    ]

    _fields_and_field_types = {
        'query': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.query = kwargs.get('query', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.query != other.query:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def query(self):
        """Message field 'query'."""
        return self._query

    @query.setter
    def query(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'query' field must be of type 'str'"
        self._query = value


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_Query_Response(type):
    """Metaclass of message 'Query_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('robopoint_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'robopoint_interfaces.srv.Query_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__query__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__query__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__query__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__query__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__query__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Query_Response(metaclass=Metaclass_Query_Response):
    """Message class 'Query_Response'."""

    __slots__ = [
    ]

    _fields_and_field_types = {
    }

    SLOT_TYPES = (
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)


class Metaclass_Query(type):
    """Metaclass of service 'Query'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('robopoint_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'robopoint_interfaces.srv.Query')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__query

            from robopoint_interfaces.srv import _query
            if _query.Metaclass_Query_Request._TYPE_SUPPORT is None:
                _query.Metaclass_Query_Request.__import_type_support__()
            if _query.Metaclass_Query_Response._TYPE_SUPPORT is None:
                _query.Metaclass_Query_Response.__import_type_support__()


class Query(metaclass=Metaclass_Query):
    from robopoint_interfaces.srv._query import Query_Request as Request
    from robopoint_interfaces.srv._query import Query_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
