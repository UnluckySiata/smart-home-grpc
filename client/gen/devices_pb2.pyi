from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SensorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPERATURE: _ClassVar[SensorType]
    AIR_QUALITY: _ClassVar[SensorType]

class ReplyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OK: _ClassVar[ReplyType]
    ERR: _ClassVar[ReplyType]
TEMPERATURE: SensorType
AIR_QUALITY: SensorType
OK: ReplyType
ERR: ReplyType

class Sensor(_message.Message):
    __slots__ = ("id", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: SensorType
    def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[SensorType, str]] = ...) -> None: ...

class Sensors(_message.Message):
    __slots__ = ("replyType", "msg", "list")
    REPLYTYPE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    replyType: ReplyType
    msg: str
    list: _containers.RepeatedCompositeFieldContainer[Sensor]
    def __init__(self, replyType: _Optional[_Union[ReplyType, str]] = ..., msg: _Optional[str] = ..., list: _Optional[_Iterable[_Union[Sensor, _Mapping]]] = ...) -> None: ...

class UnitInfo(_message.Message):
    __slots__ = ("sensorId", "unit")
    SENSORID_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    sensorId: int
    unit: str
    def __init__(self, sensorId: _Optional[int] = ..., unit: _Optional[str] = ...) -> None: ...

class Measurement(_message.Message):
    __slots__ = ("replyType", "msg", "value", "unit")
    REPLYTYPE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    replyType: ReplyType
    msg: str
    value: float
    unit: str
    def __init__(self, replyType: _Optional[_Union[ReplyType, str]] = ..., msg: _Optional[str] = ..., value: _Optional[float] = ..., unit: _Optional[str] = ...) -> None: ...

class Speaker(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class Speakers(_message.Message):
    __slots__ = ("replyType", "msg", "list")
    REPLYTYPE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    replyType: ReplyType
    msg: str
    list: _containers.RepeatedCompositeFieldContainer[Speaker]
    def __init__(self, replyType: _Optional[_Union[ReplyType, str]] = ..., msg: _Optional[str] = ..., list: _Optional[_Iterable[_Union[Speaker, _Mapping]]] = ...) -> None: ...

class SpeakerSetting(_message.Message):
    __slots__ = ("speakerId", "type", "text", "numeric")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOLUME: _ClassVar[SpeakerSetting.Type]
        SONG: _ClassVar[SpeakerSetting.Type]
    VOLUME: SpeakerSetting.Type
    SONG: SpeakerSetting.Type
    SPEAKERID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NUMERIC_FIELD_NUMBER: _ClassVar[int]
    speakerId: int
    type: SpeakerSetting.Type
    text: str
    numeric: float
    def __init__(self, speakerId: _Optional[int] = ..., type: _Optional[_Union[SpeakerSetting.Type, str]] = ..., text: _Optional[str] = ..., numeric: _Optional[float] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ("type", "msg")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    type: ReplyType
    msg: str
    def __init__(self, type: _Optional[_Union[ReplyType, str]] = ..., msg: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
