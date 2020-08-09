from rpc_microservice import AcmeRPCMicroservice

acme_rpc_microservice = AcmeRPCMicroservice()


class TestAcmeRPCMicroService:

    def test_square_odd_numbers(self):
        items = list(range(0, 10))
        squared_odd_numbers = acme_rpc_microservice.square_odd_numbers(items)
        assert squared_odd_numbers == [0, 4, 16, 36, 64]

    def test_huffman_encode_strings(self):
        items = ["Acme Bricks", "Contoso.com", "Hubris Software"]
        encoded_strings = acme_rpc_microservice.huffman_encode_strings(items)
        assert "Acme Bricks" in encoded_strings.keys() \
                and encoded_strings["Acme Bricks"] == "" \
                and "Contoso.com" in encoded_strings.keys() \
                and encoded_strings["Contoso.com"] == "" \

    def test_decode_huffman_encoded_string(self):
        item = acme_rpc_microservice.huffman_encode_strings(["Hubris Software"])
        decoded_string = acme_rpc_microservice.decode_huffman_encoded_string(
                item)
        assert decoded_string != ""

