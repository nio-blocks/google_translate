from nio.block.base import Block
from nio.properties import VersionProperty, StringProperty
from nio.signal.base import Signal

from googletrans import Translator

class GoogleTranslate(Block):

    version = VersionProperty('0.1.0')
    src = StringProperty(title='Source Language')
    dest = StringProperty(title='Destination Language')
  
    def __init__(self):
        super().__init__()
        self.translator = None

    def start(self):
        self.translator = Translator()

    def process_signals(self, signals):
        fresh_signals = []

        for signal in signals:
            tmp = Signal()
            translated_text = translator.translate(signal.text, src=src, dest=dest).text.encode('utf-8')
            fresh_signals.append(setattr(tmp, 'text', translated_text))

        signals = fresh_signals
            
        self.notify_signals(signals)
