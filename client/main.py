import grpc
from gen import devices_pb2, devices_pb2_grpc

if __name__ == "__main__":
    with grpc.insecure_channel("localhost:50051") as ch:
        stub = devices_pb2_grpc.SensorServiceStub(ch)
        req_body = devices_pb2.Empty()
        r = stub.GetSensors(req_body)

        print(r.msg)

