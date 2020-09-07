#!/bin/bash 

# Cleanup
rm rpc.proto
rm rpc_pb2.py
rm rpc_pb2_grpc.py 

if [ -d googleapis ]
then
	cd googleapis \
	&& git pull \
	&& cd ..
else
	git clone https://github.com/googleapis/googleapis.git
fi
curl -o rpc.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/rpc.proto
python -m grpc_tools.protoc --proto_path=googleapis:. --python_out=. --grpc_python_out=. rpc.proto
