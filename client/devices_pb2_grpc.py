# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import devices_pb2 as devices__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in devices_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class SensorServiceStub(object):
    """services
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMeasurement = channel.unary_unary(
                '/devices.SensorService/GetMeasurement',
                request_serializer=devices__pb2.Sensor.SerializeToString,
                response_deserializer=devices__pb2.Measurement.FromString,
                _registered_method=True)
        self.SetUnit = channel.unary_unary(
                '/devices.SensorService/SetUnit',
                request_serializer=devices__pb2.UnitInfo.SerializeToString,
                response_deserializer=devices__pb2.Reply.FromString,
                _registered_method=True)
        self.GetSensors = channel.unary_unary(
                '/devices.SensorService/GetSensors',
                request_serializer=devices__pb2.Empty.SerializeToString,
                response_deserializer=devices__pb2.Sensors.FromString,
                _registered_method=True)


class SensorServiceServicer(object):
    """services
    """

    def GetMeasurement(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetUnit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSensors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SensorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMeasurement': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMeasurement,
                    request_deserializer=devices__pb2.Sensor.FromString,
                    response_serializer=devices__pb2.Measurement.SerializeToString,
            ),
            'SetUnit': grpc.unary_unary_rpc_method_handler(
                    servicer.SetUnit,
                    request_deserializer=devices__pb2.UnitInfo.FromString,
                    response_serializer=devices__pb2.Reply.SerializeToString,
            ),
            'GetSensors': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSensors,
                    request_deserializer=devices__pb2.Empty.FromString,
                    response_serializer=devices__pb2.Sensors.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'devices.SensorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SensorService(object):
    """services
    """

    @staticmethod
    def GetMeasurement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/devices.SensorService/GetMeasurement',
            devices__pb2.Sensor.SerializeToString,
            devices__pb2.Measurement.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetUnit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/devices.SensorService/SetUnit',
            devices__pb2.UnitInfo.SerializeToString,
            devices__pb2.Reply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSensors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/devices.SensorService/GetSensors',
            devices__pb2.Empty.SerializeToString,
            devices__pb2.Sensors.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class SpeakerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCurrentlyPlaying = channel.unary_unary(
                '/devices.SpeakerService/GetCurrentlyPlaying',
                request_serializer=devices__pb2.Speaker.SerializeToString,
                response_deserializer=devices__pb2.Reply.FromString,
                _registered_method=True)
        self.ApplySetting = channel.unary_unary(
                '/devices.SpeakerService/ApplySetting',
                request_serializer=devices__pb2.SpeakerSetting.SerializeToString,
                response_deserializer=devices__pb2.Reply.FromString,
                _registered_method=True)
        self.GetSpeakers = channel.unary_unary(
                '/devices.SpeakerService/GetSpeakers',
                request_serializer=devices__pb2.Empty.SerializeToString,
                response_deserializer=devices__pb2.Speakers.FromString,
                _registered_method=True)


class SpeakerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCurrentlyPlaying(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ApplySetting(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSpeakers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpeakerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCurrentlyPlaying': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCurrentlyPlaying,
                    request_deserializer=devices__pb2.Speaker.FromString,
                    response_serializer=devices__pb2.Reply.SerializeToString,
            ),
            'ApplySetting': grpc.unary_unary_rpc_method_handler(
                    servicer.ApplySetting,
                    request_deserializer=devices__pb2.SpeakerSetting.FromString,
                    response_serializer=devices__pb2.Reply.SerializeToString,
            ),
            'GetSpeakers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSpeakers,
                    request_deserializer=devices__pb2.Empty.FromString,
                    response_serializer=devices__pb2.Speakers.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'devices.SpeakerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SpeakerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCurrentlyPlaying(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/devices.SpeakerService/GetCurrentlyPlaying',
            devices__pb2.Speaker.SerializeToString,
            devices__pb2.Reply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ApplySetting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/devices.SpeakerService/ApplySetting',
            devices__pb2.SpeakerSetting.SerializeToString,
            devices__pb2.Reply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSpeakers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/devices.SpeakerService/GetSpeakers',
            devices__pb2.Empty.SerializeToString,
            devices__pb2.Speakers.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
