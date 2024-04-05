import unittest


class ImportProtoTest(unittest.TestCase):

    def test(self):
        from proto.bar.baz_pb2 import beta
        from proto.foo_pb2 import alpha

        a = alpha(ein=1)
        b = beta(zwei=2)
        self.assertEqual(a.ein, 1)
        self.assertEqual(b.zwei, 2)

if __name__ == '__main__':
    unittest.main()