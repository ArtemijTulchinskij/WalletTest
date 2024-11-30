import grpc
from concurrent import futures
import time

# Импорт сгенерированных Python-модулей
import auth_pb2
import auth_pb2_grpc
import common_pb2
import transfer_pb2
import transfer_pb2_grpc

# Реализация AuthService
class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def GetSentence(self, request, context):
        print(f"WalletAddress: {request.walletAddress}")
        return auth_pb2.GetSentenceReply(
            sentence="Test sentence for signing",
            result=common_pb2.RequestResult(
                isSuccess=True,
                errors=[],
                errorTrace=""
            )
        )

    def AuthByWalletSign(self, request, context):
        print(f"WalletAddress: {request.walletAddress}")
        print(f"SignedSentence: {request.signedSentence}")
        print(f"Chain: {request.chain}")

        # Проверка на корректность поля chain
        if request.chain not in [0, 1, 2]:  # 0 = Unknown, 1 = Solana, 2 = Ethereum
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Unsupported blockchain type")

        return auth_pb2.AuthReply(
            result=common_pb2.RequestResult(
                isSuccess=True,
                errors=[],
                errorTrace=""
            ),
            token=common_pb2.AuthTokens(
                accessToken="test_access_token",
                refreshToken="test_refresh_token"
            ),
            newTerms="",
            seedPhrase=""
        )

# Реализация TransferService
class TransferService(transfer_pb2_grpc.TransferServiceServicer):
    def GetTransfers(self, request, context):
        print(f"Chain: {request.chain}, Status Filter: {request.status}, Type Filter: {request.type}")
        return transfer_pb2.GetTransfersReply(
            result=common_pb2.RequestResult(
                isSuccess=True,
                errors=[],
                errorTrace=""
            ),
            transfers=[
                transfer_pb2.GetTransfersReplyItem(
                    hash="sample_tx_hash",
                    type=2,  # TransactionType_Transfer
                    status=2,  # TransactionStatus_Confirmed
                    amount=common_pb2.Decimals(value=1000, exp=2),
                    isHidden=False
                )
            ]
        )

    def Transfer(self, request, context):
        print(f"Amount: {request.amount}, From: {request.withdrawAddress}, To: {request.depositAddress}, Chain: {request.chain}")
        return transfer_pb2.TransferReply(
            result=common_pb2.RequestResult(
                isSuccess=True,
                errors=[],
                errorTrace=""
            ),
            hash=["sample_transfer_hash"]
        )

    def GetTransfersStream(self, request, context):
        print(f"Stream Request Received: Chain: {request.chain}, Type: {request.type}, Status: {request.status}")
        for i in range(3):  # Возвращаем 3 фиктивные транзакции
            yield transfer_pb2.GetTransfersReply(
                result=common_pb2.RequestResult(
                    isSuccess=True,
                    errors=[],
                    errorTrace=""
                ),
                transfers=[
                    transfer_pb2.GetTransfersReplyItem(
                        hash=f"stream_tx_hash_{i}",
                        type=2,  # TransactionType_Transfer
                        status=2,  # TransactionStatus_Confirmed
                        amount=common_pb2.Decimals(value=1000 + i, exp=2),
                        isHidden=False
                    )
                ]
            )

# Функция запуска сервера
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Добавление сервисов в сервер
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    transfer_pb2_grpc.add_TransferServiceServicer_to_server(TransferService(), server)

    # Запуск сервера на порту 50051
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")

    try:
        while True:
            time.sleep(86400)  # Сервер работает в течение суток
    except KeyboardInterrupt:
        server.stop(0)
        print("Server stopped")

if __name__ == "__main__":
    serve()



