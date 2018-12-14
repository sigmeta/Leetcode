class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary="{:0>32s}".format(bin(n)[2:])
        binary=binary[::-1]
        return int(binary,2)
