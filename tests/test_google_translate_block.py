from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..google_translate_block import GoogleTranslate


class TestGoogleTranslate(NIOBlockTestCase):

    def test_process_signals(self):
        """Signals pass through block unmodified."""
        blk = GoogleTranslate()
        self.configure_block(blk, {'src': 'en', 'dest': 'fr'})
        blk.start()
        blk.process_signals([Signal({"text": "hello"})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"text": "Bonjour"})
