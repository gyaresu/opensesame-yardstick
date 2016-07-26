import bitstring


def makeKey(key, state):
    """Return packet string: 110 for '1' and 100 for '0'
    Deal with binary / trinary dip switch state."""
    if(key[0:1] == "1"):
        key = "1" + key
    pwm_str_key = ""
    for k in key:
        x = "*"
        if(k == "1"):
            x = "1110"
        if(k == "0"):
            x = "1000"
        if(k == "x"):
            x = "0000"
        pwm_str_key = pwm_str_key + x
        #print pwm_str_key
    key_packed = bitstring.BitArray(bin=pwm_str_key).tobytes()
    return key_packed
