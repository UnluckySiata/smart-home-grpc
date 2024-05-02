srv_out=server/gen
client_out=client/gen
proto_files=devices.proto

gen: $(proto_files)
	mkdir -p $(srv_out) $(client_out)
	touch $(client_out)/__init__.py
	protoc --go_out=$(srv_out) --go_opt=paths=source_relative --go-grpc_out=$(srv_out) --go-grpc_opt=paths=source_relative $(proto_files)
	python -m grpc_tools.protoc -I. --python_out=$(client_out) --pyi_out=$(client_out) --grpc_python_out=$(client_out) $(proto_files)
