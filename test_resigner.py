import unittest
from resigner import Resigner


class TestResigner(unittest.TestCase):
    INVALID_PREAMBLE = "0300000002012c866bd675ad11475ea608dea4d9d166801f1725b207636363d55508aa07ba6f000000005b17b90d04683625c2445a4e9564bf710c5528fd99a7d150d2a2a323bc22ff9e2710da4f6d00000011000000010000000008000000000000000289b5a4e5e20c56512c64967dfa72e67c39166d5c48ad6884693c7d192e105c3b00058f7b73557941607800"
    VALID_BLOCK = "0100000002012c866bd675ad11475ea608dea4d9d166801f1725b207636363d55508aa07ba6f000000005b17b90d04683625c2445a4e9564bf710c5528fd99a7d150d2a2a323bc22ff9e2710da4f6d00000011000000010000000008000000000000000289b5a4e5e20c56512c64967dfa72e67c39166d5c48ad6884693c7d192e105c3b00058f7b73557941607800"
    VALID_ENDORSEMENT = "02e49ddfcff83062bae835a34f07d4b0d6c795d6b062385a656afa6487f9ffa6a90000000002e49ddfcff83062bae835a34f07d4b0d6c795d6b062385a656afa6487f9ffa6a90000001800000018000000100000000b0000000a0000000800000001"

    def test_identifies_invalid_block_preamble(self):
        rs = Resigner(self.INVALID_PREAMBLE)
        self.assertFalse(rs.is_block())

    def test_identifies_valid_block_preamble(self):
        rs = Resigner(self.VALID_BLOCK)
        self.assertTrue(rs.is_block())

    def test_identifies_valid_endorsement_preamble(self):
        rs = Resigner(self.VALID_ENDORSEMENT)
        self.assertTrue(rs.is_endorsement())

    def test_decodes_block_level(self):
        rs = Resigner(self.VALID_BLOCK)
        self.assertEqual(rs.get_block_level(), 2)

    def test_succeeds_if_level_in_threshold(self):
        class DummyRPCClient:
            def get_current_level(self):
                return 1

        rs = Resigner(self.VALID_BLOCK, DummyRPCClient())
        self.assertTrue(rs.is_within_level_threshold())


if __name__ == '__main__':
    unittest.main()