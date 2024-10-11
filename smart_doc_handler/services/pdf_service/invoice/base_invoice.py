from abc import ABC, abstractmethod

class BaseInvoice(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def extract_data(self):
        pass
