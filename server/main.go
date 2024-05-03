package main

import (
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

func main() {
	flag.Parse()
	listener, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()

	sensors := &sensorServer{
		sensors: []*pb.Sensor{
			{Id: 0, Type: pb.SensorType_TEMPERATURE, Value: 0.5, Unit: "Celcius"},
			{Id: 1, Type: pb.SensorType_PRESSURE, Value: 0.4, Unit: "hPa"},
		},
	}

	speakers := &speakerServer{
		speakers: []*pb.Speaker{
			{Id: 0},
			{Id: 1},
		},
	}

	pb.RegisterSpeakerServiceServer(s, speakers)
	pb.RegisterSensorServiceServer(s, sensors)

	log.Printf("server listening at %v", listener.Addr())
	if err := s.Serve(listener); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
