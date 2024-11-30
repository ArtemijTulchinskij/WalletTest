import grpc
import auth_pb2
import auth_pb2_grpc
import transfer_pb2
import transfer_pb2_grpc

def run():
    # Подключение к серверу
    channel = grpc.insecure_channel('localhost:50051')

    # Авторизация
    auth_stub = auth_pb2_grpc.AuthServiceStub(channel)
    login_response = auth_stub.Login(auth_pb2.LoginRequest(username="test", password="password"))
    print("Токен авторизации:", login_response.token)

    # Перевод криптовалюты
    transfer_stub = transfer_pb2_grpc.TransferServiceStub(channel)
    transfer_response = transfer_stub.Transfer(transfer_pb2.TransferRequest(
        from_address="addr1",
        to_address="addr2",
        amount=10.0
    ))
    print("Хеш перевода:", transfer_response.hash)

    # Проверка статуса
    status_response = transfer_stub.CheckStatus(transfer_pb2.CheckStatusRequest(hash=transfer_response.hash))
    print("Статус транзакции:", status_response.status)

if __name__ == "__main__":
    run()
