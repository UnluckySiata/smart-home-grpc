package main

import (
	"context"

	pb "github.com/unluckysiata/smart-home-grpc/server/gen"
)

type speakerServer struct {
	pb.UnimplementedSpeakerServiceServer

	speakers []*pb.Speaker
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
