from src.gui.chat import ChatGUI
from src.libs.rpc.objects import Censor
from src.libs.tuple_space import TupleSpace, AbstractTupleSpace
from src.repository.message import MessageRepository
from src.repository.spy import SpyRepository
from src.repository.user import UserRepository

if __name__ == "__main__":
    tuple_space: AbstractTupleSpace = TupleSpace()
    services = {
        "user_repository": UserRepository(tuple_space=tuple_space),
        "message_repository": MessageRepository(tuple_space=tuple_space),
        "spy_repository": SpyRepository(tuple_space=tuple_space),
        "censor": Censor.get(),
    }

    chat_gui: ChatGUI = ChatGUI(services=services)
    chat_gui.run()
