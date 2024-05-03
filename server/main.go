package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"

	pb "github.com/unluckysiata/smart-home-grpc/server/gen"
	"google.golang.org/grpc"
)

var (
	port = flag.Int("port", 50051, "The server port")
)

type sensorServer struct {
	pb.UnimplementedSensorServiceServer
}

func (s *sensorServer) GetMeasurement(ctx context.Context, in *pb.Sensor) (*pb.Measurement, error) {
	return &pb.Measurement{}, nil
}

func (s *sensorServer) SetUnit(ctx context.Context, in *pb.UnitInfo) (*pb.Reply, error) {
	return &pb.Reply{}, nil
}

func (s *sensorServer) GetSensors(ctx context.Context, in *pb.Empty) (*pb.Sensors, error) {
	return &pb.Sensors{ReplyType: pb.ReplyType_ERR, Msg: "No sensors registered"}, nil
}

type speakerServer struct {
	pb.UnimplementedSpeakerServiceServer
}

func (s *speakerServer) GetCurrentlyPlaying(ctx context.Context, in *pb.Speaker) (*pb.Reply, error) {
	return &pb.Reply{}, nil
}

func (s *speakerServer) ApplySetting(ctx context.Context, in *pb.SpeakerSetting) (*pb.Reply, error) {
	return &pb.Reply{}, nil
}

func (s *speakerServer) GetSpeakers(ctx context.Context, in *pb.Empty) (*pb.Speakers, error) {
	return &pb.Speakers{ReplyType: pb.ReplyType_ERR, Msg: "No speakers registered"}, nil
}

func main() {
	flag.Parse()
	listener, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()

	pb.RegisterSpeakerServiceServer(s, &speakerServer{})
	pb.RegisterSensorServiceServer(s, &sensorServer{})

	log.Printf("server listening at %v", listener.Addr())
	if err := s.Serve(listener); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
