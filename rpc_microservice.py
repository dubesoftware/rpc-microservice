from nameko.rpc import rpc


from dahuffman import HuffmanCodec


class AcmeRPCMicroservice:
    """A sample RPC microservice using the Nameko framework."""

    name = "acme_rpc_microservice"

    @rpc
    def square_odd_numbers(self, items):
        """Square each odd number in a given list of integers.

        Parameters:
            items (list): -- a list of integers.

        Returns:
            A list of odd integers squared.
        """
        return [item ** 2 for item in items if item % 2 == 1]

    @rpc
    def huffman_encode_strings(self, items):
        """Build a dictionary of strings - the key being the original string, 
        and the value being a (Huffman) encoded version of that string.

        Parameters:
            items (list): a list of strings.

        Returns:
            A dictionary of Huffman encoded strings with original strings as 
            keys and encoded strings as values.
        """
        encoded_items = {}
        for item in items:
            item_codec = HuffmanCodec.from_data(item)
            encoded_item = item_codec.encode(item)
            encoded_items.update({item: encoded_item})
        return encoded_items

    @rpc
    def decode_huffman_encoded_string(self, item):
        """Decode a given string previously Huffman encoded.

        Parameters:
            item (string): a Huffman encoded string.

        Returns:
            A decoded string.
        """
        return "" 

