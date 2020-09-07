import rpc_pb2 as ln
import rpc_pb2_grpc as lnrpc
import grpc
import os

import codecs


with open('/mnt/hdd/lnd/data/chain/bitcoin/mainnet/admin.macaroon', 'rb') as f:
    macaroon_bytes = f.read()
    macaroon = codecs.encode(macaroon_bytes, 'hex')

os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

cert = open('/mnt/hdd/lnd/tls.cert', 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('localhost:10009', creds)
stub = lnrpc.LightningStub(channel)

response = stub.WalletBalance(ln.WalletBalanceRequest(), metadata=[('macaroon', macaroon)])
print(response.total_balance)



request = ln.ChannelBackupSubscription()
for response in stub.SubscribeChannelBackups(request, metadata=[('macaroon', macaroon)]):
    print(response)
