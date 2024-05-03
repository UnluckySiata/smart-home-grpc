import grpc
import devices_pb2
import devices_pb2_grpc

servers: list[str] = ["localhost:50051"]
n = len(servers)
channels: list[grpc.Channel] = []
stubs: list[tuple[devices_pb2_grpc.SensorServiceStub, devices_pb2_grpc.SpeakerServiceStub]] = []


def stringify_sensors(sensors):
    res = ""

    for s in sensors:
        repr = f"id: {s.id}, type: {'temperature' if s.type == devices_pb2.SensorType.TEMPERATURE else 'pressure'}\n"
        res += repr
    return res


def stringify_speakers(speakers):
    res = ""

    for s in speakers:
        repr = f"id: {s.id}\n"
        res += repr
    return res


def handle_list(r1, r2):
    if r1.replyType == devices_pb2.ReplyType.OK:
        print(f"Sensors from server {server}:\n{stringify_sensors(r1.list)}")
    else:
        print(f"Got message from {server}: {r1.msg}")

    if r2.replyType == devices_pb2.ReplyType.OK:
        print(f"Speakers from server {server}:\n{stringify_speakers(r2.list)}")
    else:
        print(f"Got message from {server}: {r2.msg}")


def print_measurement(r):
    if r.replyType == devices_pb2.ReplyType.OK:
        print(f"{r.value} {r.unit}")
    else:
        print(r.msg)

def print_help():
    h = """
Commands:
[h]elp - print this message
[l]ist devices from a server
[i]nteract with a device from a server
[e]xit
"""
    print(h)


if __name__ == "__main__":
    print(f"Available servers: {', '.join(servers)}")
    for server in servers:
        ch = grpc.insecure_channel(server)
        sensor_stub = devices_pb2_grpc.SensorServiceStub(ch)
        speaker_stub = devices_pb2_grpc.SpeakerServiceStub(ch)

        req_body = devices_pb2.Empty()
        r1 = sensor_stub.GetSensors(req_body)
        r2 = speaker_stub.GetSpeakers(req_body)

        channels.append(ch)
        stubs.append((sensor_stub, speaker_stub))

        handle_list(r1, r2)

    print_help()
    while True:
        match input("> ").lower():
            case "h":
                print_help()
            case "l":
                print(f"select from available servers:\n{', '.join([f'{i}: {servers[i]}' for i in range(n)])}")
                selected = int(input("> "))
                if selected < 0 or selected >= n:
                    print("wrong selection")
                    continue

                sensor_stub, speaker_stub = stubs[selected]

                req_body = devices_pb2.Empty()
                r1 = sensor_stub.GetSensors(req_body)
                r2 = speaker_stub.GetSpeakers(req_body)

                handle_list(r1, r2)

            case "i":
                print(f"select from available servers:\n{', '.join([f'{i}: {servers[i]}' for i in range(n)])}")
                selected = int(input("> "))
                if selected < 0 or selected >= n:
                    print("wrong selection")
                    continue

                sensor_stub, speaker_stub = stubs[selected]

                selected = int(input("Enter device id: "))
                while True:
                    match input("Enter device type from [se]nsor, [sp]eaker: ").lower():
                        case "se":
                            while True:
                                match input("Select action from [g]et, [s]et, [e]xit: " ).lower():
                                    case "g":
                                        r = sensor_stub.GetMeasurement(devices_pb2.Sensor(id=selected))

                                        print_measurement(r)
                                    case "s":
                                        unit = input("New unit: ")
                                        r = sensor_stub.SetUnit(devices_pb2.UnitInfo(sensorId=selected, unit=unit))
                                    case "e":
                                        break
                                    case _:
                                        continue
                            break
                        case "sp":
                            break
                        case _:
                            continue


            case "e":
                break
            case _:
                continue

    for ch in channels:
        ch.close()
