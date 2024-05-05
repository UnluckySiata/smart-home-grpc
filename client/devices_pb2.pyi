from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SensorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPERATURE: _ClassVar[SensorType]
    PRESSURE: _ClassVar[SensorType]

class TemperatureUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CELCIUS: _ClassVar[TemperatureUnit]
    FAHRENHEIT: _ClassVar[TemperatureUnit]

class PressureUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HPA: _ClassVar[PressureUnit]
    BAR: _ClassVar[PressureUnit]

class ReplyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OK: _ClassVar[ReplyType]
    ERR: _ClassVar[ReplyType]
TEMPERATURE: SensorType
PRESSURE: SensorType
CELCIUS: TemperatureUnit
FAHRENHEIT: TemperatureUnit
HPA: PressureUnit
BAR: PressureUnit
OK: ReplyType
ERR: ReplyType

class Sensor(_message.Message):
    __slots__ = ("id", "type", "value", "temperatureUnit", "pressureUnit")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATUREUNIT_FIELD_NUMBER: _ClassVar[int]
    PRESSUREUNIT_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: SensorType
    value: float
    temperatureUnit: TemperatureUnit
    pressureUnit: PressureUnit
    def __init__(self, id: _Optional[int] = ..., type: _Optional[_Union[SensorType, str]] = ..., value: _Optional[float] = ..., temperatureUnit: _Optional[_Union[TemperatureUnit, str]] = ..., pressureUnit: _Optional[_Union[PressureUnit, str]] = ...) -> None: ...

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
    __slots__ = ("sensorId", "type", "temperatureUnit", "pressureUnit")
    SENSORID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATUREUNIT_FIELD_NUMBER: _ClassVar[int]
    PRESSUREUNIT_FIELD_NUMBER: _ClassVar[int]
    sensorId: int
    type: SensorType
    temperatureUnit: TemperatureUnit
    pressureUnit: PressureUnit
    def __init__(self, sensorId: _Optional[int] = ..., type: _Optional[_Union[SensorType, str]] = ..., temperatureUnit: _Optional[_Union[TemperatureUnit, str]] = ..., pressureUnit: _Optional[_Union[PressureUnit, str]] = ...) -> None: ...

class Measurement(_message.Message):
    __slots__ = ("replyType", "msg", "value", "type", "temperatureUnit", "pressureUnit")
    REPLYTYPE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATUREUNIT_FIELD_NUMBER: _ClassVar[int]
    PRESSUREUNIT_FIELD_NUMBER: _ClassVar[int]
    replyType: ReplyType
    msg: str
    value: float
    type: SensorType
    temperatureUnit: TemperatureUnit
    pressureUnit: PressureUnit
    def __init__(self, replyType: _Optional[_Union[ReplyType, str]] = ..., msg: _Optional[str] = ..., value: _Optional[float] = ..., type: _Optional[_Union[SensorType, str]] = ..., temperatureUnit: _Optional[_Union[TemperatureUnit, str]] = ..., pressureUnit: _Optional[_Union[PressureUnit, str]] = ...) -> None: ...

class Speaker(_message.Message):
    __slots__ = ("id", "song", "volume")
    ID_FIELD_NUMBER: _ClassVar[int]
    SONG_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    id: int
    song: str
    volume: int
    def __init__(self, id: _Optional[int] = ..., song: _Optional[str] = ..., volume: _Optional[int] = ...) -> None: ...

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
    numeric: int
    def __init__(self, speakerId: _Optional[int] = ..., type: _Optional[_Union[SpeakerSetting.Type, str]] = ..., text: _Optional[str] = ..., numeric: _Optional[int] = ...) -> None: ...

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
