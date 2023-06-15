from abc import ABC, abstractmethod


class Mimo(ABC):

    @abstractmethod
    def create_message_service(self, token: str):
        pass

    
    @abstractmethod
    def create_campain_service(self, token: str):
        pass


    @abstractmethod
    def create_sender_service(self, token: str):
        pass


class CampainService:
    def __init__(self, token: str) -> None:
        pass


class MessageService:
    def __init__(self, token: str) -> None:
        pass

    @staticmethod
    def build(token: str):
        return MessageService(token)
    
    def send_sms(self, *, sender: str, receivers: list, text: str):
        print("SENDER: ", sender, "=>", receivers, "=>", text)


class SenderService:
    def __init__(self, token: str) -> None:
        pass


class MimoService(Mimo):
    def create_campain_service(self, token: str) -> CampainService:
        return CampainService(token)
    
    def create_message_service(self, token: str) -> MessageService:
        return MessageService.build(token)
    
    def create_sender_service(self, token: str) -> SenderService:
        return SenderService(token)


mimo_service = MimoService()
message_service = mimo_service.create_message_service("some_token")
message_service.send_sms(sender="SATURNO", receivers=["933843893"], text="Olá, Mundo!")
