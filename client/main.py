import grpc
import devices_pb2
import devices_pb2_grpc

# servers: list[str] = ["localhost:50051"]
servers: list[str] = ["localhost:50051", "localhost:50052"]
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


def handle_list(r1, r2, server):
    if r1.replyType == devices_pb2.ReplyType.OK:
        print(f"Sensors from server {server}:\n{stringify_sensors(r1.list)}")
    else:
        print(f"Got message from {server}: {r1.msg}")

    if r2.replyType == devices_pb2.ReplyType.OK:
        print(f"Speakers from server {server}:\n{stringify_speakers(r2.list)}")
    else:
        print(f"Got message from {server}: {r2.msg}")


def print_measurement(r):
    unit: str
    if r.replyType == devices_pb2.ReplyType.OK:
        match r.type:
            case devices_pb2.TEMPERATURE:
                match r.temperatureUnit:
                    case devices_pb2.CELCIUS:
                        unit = "C"
                    case devices_pb2.FAHRENHEIT:
                        unit = "F"
                    case _:
                        unit = "unknown"

            case devices_pb2.PRESSURE:
                match r.pressureUnit:
                    case devices_pb2.BAR:
                        unit = "Ba"
                    case devices_pb2.HPA:
                        unit = "hPa"
                    case _:
                        unit = "unknown"
            case _:
                unit = "unknown"


        print(f"{r.value} {unit}")
    else:
        print(r.msg)

def print_help():
    h = """
Commands:
[h]elp - print this message
[s]ervers (print available)
[d]evice types (print all)
[l]ist devices from a server:
l <server_id>
[i]nteract with a device from a server
i <server_id> <device_type> <device_id> <action> <values...>
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

        handle_list(r1, r2, server)

    print_help()
    while True:
        cmd = input("> ")
        if len(cmd) < 1:
            continue
        match cmd[0]:
            case "h":
                print_help()
            case "s":
                print(f"Available servers:\n{', '.join([f'{i}: {servers[i]}' for i in range(n)])}")
            case "d":
                print("Device types:\n[se]nsor\n[sp]eaker")
            case "l":
                selected = int(cmd[2:])
                if selected < 0 or selected >= n:
                    print(f"Not a valid server id: {selected}")
                    continue

                sensor_stub, speaker_stub = stubs[selected]

                req_body = devices_pb2.Empty()
                r1 = sensor_stub.GetSensors(req_body)
                r2 = speaker_stub.GetSpeakers(req_body)

                handle_list(r1, r2, servers[selected])

            case "i":
                l = cmd[2:].split(sep=" ")
                selected_server = int(l[0])
                device_type = l[1].lower()
                selected_device = int(l[2])
                action = l[3].lower()
                values = l[4:]
                if selected_server < 0 or selected_server >= n:
                    print(f"Not a valid server id: {selected_server}")
                    continue

                sensor_stub, speaker_stub = stubs[selected_server]

                match device_type:
                    case "se":
                        match action:
                            case "g":
                                r = sensor_stub.GetMeasurement(devices_pb2.Sensor(id=selected_device))

                                print_measurement(r)

                            case "s":
                                match values[0]:
                                    case "c":
                                        unit = devices_pb2.CELCIUS
                                        t = devices_pb2.TEMPERATURE
                                        r = sensor_stub.SetUnit(devices_pb2.UnitInfo(sensorId=selected_device, type=t, temperatureUnit=unit))
                                    case "f":
                                        unit = devices_pb2.FAHRENHEIT
                                        t = devices_pb2.TEMPERATURE
                                        r = sensor_stub.SetUnit(devices_pb2.UnitInfo(sensorId=selected_device, type=t, temperatureUnit=unit))
                                    case "ba":
                                        unit = devices_pb2.BAR
                                        t = devices_pb2.PRESSURE
                                        r = sensor_stub.SetUnit(devices_pb2.UnitInfo(sensorId=selected_device, type=t, pressureUnit=unit))
                                    case "hpa":
                                        unit = devices_pb2.HPA
                                        t = devices_pb2.PRESSURE
                                        r = sensor_stub.SetUnit(devices_pb2.UnitInfo(sensorId=selected_device, type=t, pressureUnit=unit))
                                    case _:
                                        print(f"Unknown unit type: {values[0]}")
                                        continue

                                if r.type == devices_pb2.ReplyType.ERR:
                                    print(r.msg)
                                else:
                                    print("ok")
                            case _:
                                print(f"invalid action: {action}")
                    case "sp":
                        match action:
                            case "g":
                                r = speaker_stub.GetCurrentlyPlaying(devices_pb2.Speaker(id=selected_device))

                                if r.type == devices_pb2.ReplyType.OK:
                                    print(f"playing: {r.msg}")
                                else:
                                    print(r.msg)
                            case "s":
                                match values[0]:
                                    case "volume":
                                        variant = devices_pb2.SpeakerSetting.VOLUME
                                        val = int(values[1])
                                        setting = devices_pb2.SpeakerSetting(speakerId=selected_device, type=variant, numeric=val) 
                                    case "song":
                                        variant = devices_pb2.SpeakerSetting.SONG
                                        val = values[1]
                                        setting = devices_pb2.SpeakerSetting(speakerId=selected_device, type=variant, text=val) 
                                    case _:
                                        print(f"Invalid speaker setting: {values[0]}")
                                        continue

                                r = speaker_stub.ApplySetting(setting)
                                if r.type == devices_pb2.ReplyType.ERR:
                                    print(r.msg)
                                else:
                                    print("ok")
                            case _:
                                print(f"invalid action: {action}")
                    case _:
                        print(f"invalid device type: {device_type}")


            case "e":
                break
            case _:
                continue

    for ch in channels:
        ch.close()
