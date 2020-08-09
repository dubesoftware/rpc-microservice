from nameko.rpc import rpc


class AcmeRPCMicroservice:
    """A sample RPC microservice using the Nameko framework."""

    name = "acme_rpc_microservice"

    @rpc
    def square_odd_numbers(self, items):
        """Square each odd number in a given list of integers.

        Keyword arguments:
        items -- a list of integers
        """
        return ""

    @rpc
    def huffman_encode_strings(self, items):
        """Build a dictionary of strings - the key being the original string, 
        and the value being a (Huffman) encoded version of that string.

        Keyword arguments:
        items -- a list of strings
        """
        return ""       

    @rpc
    def decode_huffman_encoded_string(self, item):
        """Decode a given string previously Huffman encoded.

        Keyword arguments:
        item -- a string
        """
        return "" 

