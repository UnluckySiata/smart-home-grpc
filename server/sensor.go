package main

import (
	"context"

	pb "github.com/unluckysiata/smart-home-grpc/server/gen"
)

type sensorServer struct {
	pb.UnimplementedSensorServiceServer

	sensors []*pb.Sensor
}

func (s *sensorServer) GetMeasurement(ctx context.Context, in *pb.Sensor) (*pb.Measurement, error) {
	if uint32(len(s.sensors)) > in.Id {
		sensor := s.sensors[in.Id]
		switch sensor.Type {
		case pb.SensorType_TEMPERATURE:
			return &pb.Measurement{
				ReplyType: pb.ReplyType_OK,
				Type:      pb.SensorType_TEMPERATURE,
				Value:     sensor.Value,
				Unit:      &pb.Measurement_TemperatureUnit{TemperatureUnit: sensor.GetTemperatureUnit()}}, nil
		case pb.SensorType_PRESSURE:
			return &pb.Measurement{
				ReplyType: pb.ReplyType_OK,
				Type:      pb.SensorType_PRESSURE,
				Value:     sensor.Value,
				Unit:      &pb.Measurement_PressureUnit{PressureUnit: sensor.GetPressureUnit()}}, nil
		}
	}
	return &pb.Measurement{ReplyType: pb.ReplyType_ERR, Msg: "Sensor with given id not found!"}, nil
}

func (s *sensorServer) SetUnit(ctx context.Context, in *pb.UnitInfo) (*pb.Reply, error) {
	if uint32(len(s.sensors)) > in.SensorId {
		sensor := s.sensors[in.SensorId]

		switch sensor.Type {
		case pb.SensorType_TEMPERATURE:
			if in.GetType() != pb.SensorType_TEMPERATURE {
				return &pb.Reply{Type: pb.ReplyType_ERR, Msg: "Invalid unit type for temperature sensor"}, nil
			}
			sensor.Unit = &pb.Sensor_TemperatureUnit{TemperatureUnit: in.GetTemperatureUnit()}
		case pb.SensorType_PRESSURE:
			if in.GetType() != pb.SensorType_PRESSURE {
				return &pb.Reply{Type: pb.ReplyType_ERR, Msg: "Invalid unit type for pressure sensor"}, nil
			}
			sensor.Unit = &pb.Sensor_PressureUnit{PressureUnit: in.GetPressureUnit()}
		default:
			return &pb.Reply{Type: pb.ReplyType_ERR, Msg: "Invalid unit type"}, nil
		}
		return &pb.Reply{Type: pb.ReplyType_OK}, nil
	}
	return &pb.Reply{Type: pb.ReplyType_ERR, Msg: "Sensor with given id not found!"}, nil
}

func (s *sensorServer) GetSensors(ctx context.Context, in *pb.Empty) (*pb.Sensors, error) {
	if len(s.sensors) > 0 {
		return &pb.Sensors{ReplyType: pb.ReplyType_OK, List: s.sensors}, nil
	}
	return &pb.Sensors{ReplyType: pb.ReplyType_ERR, Msg: "No sensors registered"}, nil
}
