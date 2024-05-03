import grpc
import devices_pb2
import devices_pb2_grpc

if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as ch:
        sensor_stub = devices_pb2_grpc.SensorServiceStub(ch)
        speaker_stub = devices_pb2_grpc.SpeakerServiceStub(ch)

        req_body = devices_pb2.Empty()
        r1 = sensor_stub.GetSensors(req_body)
        r2 = speaker_stub.GetSpeakers(req_body)


        print(r1.msg, r2.msg)

