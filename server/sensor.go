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
		return &pb.Measurement{ReplyType: pb.ReplyType_OK, Value: sensor.Value, Unit: sensor.Unit}, nil
	}
	return &pb.Measurement{ReplyType: pb.ReplyType_ERR, Msg: "Sensor with given id not found!"}, nil
}

func (s *sensorServer) SetUnit(ctx context.Context, in *pb.UnitInfo) (*pb.Reply, error) {
	if uint32(len(s.sensors)) > in.SensorId {
		sensor := s.sensors[in.SensorId]
		sensor.Unit = in.Unit
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
