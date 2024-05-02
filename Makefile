out_dir=gen
proto_files=devices.proto

gen: $(proto_files)
	mkdir -p $(out_dir)/go $(out_dir)/cpp
	protoc --go_opt=paths=source_relative --go_out=$(out_dir)/go $(proto_files)
	protoc --go_out=$(out_dir)/go --go_opt=paths=source_relative --go-grpc_out=$(out_dir)/go --go-grpc_opt=paths=source_relative $(proto_files)
	# protoc --cpp_out=$(out_dir)/cpp $(proto_files)
