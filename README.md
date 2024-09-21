# Smart Home
A basic implementation of simulated smart home client/server applications
with the ability of configuring some appliances.

## Running
Type
```bash
go run ./server --port 50051
go run ./server --port 50052
```
to run both servers with preconfigured ports needed for the client
to interact with them. Then run
```bash
python3 client/main.py
```
to launch the client cli.

This mini-project was developed as a part of the distributed systems course at AGH UST.

