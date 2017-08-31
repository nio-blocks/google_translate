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
        self.translator = Translator()

    def process_signals(self, signals):
        fresh_signals = []

        for signal in signals:
            tmp = Signal()
            translated_text = self.translator.translate(signal.text,
                                                        src=self.src(),
                                                        dest=self.dest()).text
            signal.text = translated_text
            fresh_signals.append(signal)

        signals = fresh_signals

        self.notify_signals(signals)
