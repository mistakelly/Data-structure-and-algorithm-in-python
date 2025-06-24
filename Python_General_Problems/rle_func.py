"""
Custom compression algorithm.
RLE: Run-length-encoding.
"""

def rle_encode(word):
    encode= []

    count = 1

    prev_char = word[0]


    for cur_char in word[1:]:
        if cur_char == prev_char:
            count +=1
        else:
            encode.append(f'{count}{prev_char}')
            prev_char = cur_char
            count = 1
        
    encode.append(f'{count}{prev_char}')
    return encode


data = 'AAABBBCCDDE'
result = rle_encode(data)
print('encoded', result)