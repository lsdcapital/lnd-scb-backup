#!/usr/bin/python3

import datetime
import os
import rpc_pb2 as ln
import rpc_pb2_grpc as lnrpc
import grpc
import codecs

from google.protobuf.json_format import MessageToDict
from base64 import b64decode


def getConfig():
    with open('admin.macaroon', 'rb') as f:
        macaroon_bytes = f.read()
        macaroon = codecs.encode(macaroon_bytes, 'hex')

    os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

    cert = open('tls.cert', 'rb').read()
    creds = grpc.ssl_channel_credentials(cert)
    channel = grpc.secure_channel('localhost:10009', creds)
    stub = lnrpc.LightningStub(channel)

    response = stub.WalletBalance(ln.WalletBalanceRequest(), metadata=[('macaroon', macaroon)])
    print(response.total_balance)

def listen():
    request = ln.ChannelBackupSubscription()
    for response in stub.SubscribeChannelBackups(request, metadata=[('macaroon', macaroon)]):
        json_out = MessageToDict(response, including_default_value_fields=True)
        decode = b64decode(json_out["multiChanBackup"]["multiChanBackup"])
        with open('file.meep', "wb") as file:
            file.write(decode)
        
        hex = decode.hex()
        print(hex)

def upload_to_bucket(blob_name, path_to_file, bucket_name):
    """ Upload data to a bucket"""

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json('creds.json')

    #print(buckets = list(storage_client.list_buckets())

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)

    #returns a public url
    return blob.public_url

if __name__ == "__main__":
    getConfig()
    listen()
#    backupChannel()

