try:
    import grpc
    from concurrent import futures
    import  time
    import emoji
    import emoji_pb2          #This are File GRPC Generated for me
    import emoji_pb2_grpc     #This are File GRPC Generated for me
except Exception as e :
    print("error loading modules")

class EmojiServicer(emoji_pb2_grpc.EmojiServicer):

    def MessageResponse(self, request, context):
        response= emoji_pb2_grpc.Message()
        response.value=emoji.Message_Response(request.value)
        return response

def run():
    server= grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    emoji_pb2_grpc.add_EmojiServicer_to_server(EmojiServicer(), server)
    print('Starting server.Listening on port 80.')
    server.add_insecure_port('[: ::88')
    server.start()
try:
    while True:
        time.sleep(_ONE_DAY_IN_SECONDS)
except  KeyboardInterrupt:
    server.stop(0)

