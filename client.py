import grpc
import emoji_pb2
import emoji_pb2_grpc



def run():
    # Step 1: Creat a Channel
   with grpc.insecure_channel('localhost:80') as channel:
   # Step 2: Creat a  Stub
    stub = emoji_pb2_grpc.EmojiStub(channel)
   # Step 3:  call API
    response = stub.emoji(emoji_pb2.ClientInput(name='John', greeting = "Yo"))
   print("Emoji client received following from server: " + response.message)
run()

