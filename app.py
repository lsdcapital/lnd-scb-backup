import codecs, grpc, os
# Generate the following 2 modules by compiling the lnrpc/rpc.proto with the grpcio-tools.
# See https://github.com/lightningnetwork/lnd/blob/master/docs/grpc/python.md for instructions.
import rpc_pb2 as lnrpc, rpc_pb2_grpc as rpcstub
macaroon = codecs.encode(open('LND_DIR/data/chain/bitcoin/simnet/admin.macaroon', 'rb').read(), 'hex')
os.environ['GRPC_SSL_CIPHER_SUITES'] = 'HIGH+ECDSA'
cert = open('LND_DIR/tls.cert', 'rb').read()
ssl_creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('localhost:10009', ssl_creds)
stub = rpcstub.LightningStub(channel)
request = lnrpc.ChannelBackupSubscription()
for response in stub.SubscribeChannelBackups(request, metadata=[('macaroon', macaroon)]):
    print(response)
