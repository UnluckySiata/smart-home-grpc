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
	if uint32(len(s.speakers)) > in.Id {
		speaker := s.speakers[in.Id]
		return &pb.Reply{Type: pb.ReplyType_OK, Msg: speaker.Song}, nil
	}
	return &pb.Reply{Type: pb.ReplyType_ERR, Msg: "Speaker with given id not found"}, nil
}

func (s *speakerServer) ApplySetting(ctx context.Context, in *pb.SpeakerSetting) (*pb.Reply, error) {
	var speaker *pb.Speaker
	if uint32(len(s.speakers)) > in.SpeakerId {
		speaker = s.speakers[in.SpeakerId]
	} else {
		return &pb.Reply{Type: pb.ReplyType_ERR, Msg: "Speaker with given id not found"}, nil
	}

	switch in.Type {
	case pb.SpeakerSetting_SONG:
		speaker.Song = in.GetText()

	case pb.SpeakerSetting_VOLUME:
		vol := in.GetNumeric()
		if vol > 100 {
			return &pb.Reply{Type: pb.ReplyType_ERR, Msg: "Volume cannot be higher than 100"}, nil
		}
		speaker.Volume = in.GetNumeric()
	default:
		return &pb.Reply{Type: pb.ReplyType_ERR, Msg: "Unknown setting"}, nil
	}

	return &pb.Reply{Type: pb.ReplyType_OK}, nil
}

func (s *speakerServer) GetSpeakers(ctx context.Context, in *pb.Empty) (*pb.Speakers, error) {
	if len(s.speakers) > 0 {
		return &pb.Speakers{ReplyType: pb.ReplyType_OK, List: s.speakers}, nil
	}
	return &pb.Speakers{ReplyType: pb.ReplyType_ERR, Msg: "No speakers registered"}, nil
}
