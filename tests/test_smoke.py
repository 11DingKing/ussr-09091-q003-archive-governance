import unittest

from src.archive_governance.domain import ImportBatch, ImportState


class ImportSmokeTest(unittest.TestCase):
    def test_new_batch_requires_precheck(self):
        self.assertEqual(ImportBatch("demo", "sample").state, ImportState.PRECHECK)


if __name__ == "__main__":
    unittest.main()
