import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from caprover import clean_docker_logs  # noqa: E402


def frame(stream: int, line: str) -> str:
    """Docker multiplexed frame: 8-byte header (stream, 0,0,0, uint32 size) + payload."""
    size = len(line.encode())
    header = bytes([stream, 0, 0, 0]) + size.to_bytes(4, "big")
    return header.decode("latin-1") + line


class CleanDockerLogsTest(unittest.TestCase):
    def test_strips_header_with_printable_size_byte(self):
        # size 42 == '*' and 65 == 'A': printable, so a control-char filter keeps them
        raw = frame(1, "x" * 41 + "\n") + frame(2, "y" * 64 + "\n")
        self.assertEqual(clean_docker_logs(raw), "x" * 41 + "\n" + "y" * 64 + "\n")

    def test_keeps_plain_text(self):
        self.assertEqual(clean_docker_logs("hello\nworld\n"), "hello\nworld\n")

    def test_still_strips_stray_control_chars(self):
        self.assertEqual(clean_docker_logs("a\x07b\n"), "ab\n")


if __name__ == "__main__":
    unittest.main()
