import bitstring


def pwmKey(key, state):
    """Return packet string:
        Trinary: 1001 for '+', 1000 for '0', and 1001 for '-'
    Deal with binary / trinary dip switch state."""
    #if(key[0:1] == "1"):
    #    key = "1" + key
    pwm_str_key = ""
    if state == 2:
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
    elif state == 3:
        for k in key:
            x = "*"
            if(k == "0"):
                x = "1000"
            if(k == "1"):
                x = "1001"
            if(k == "2"):
                x = "1011"
            if(k == "x"):
                x = "0000"
            pwm_str_key = pwm_str_key + x
        pwm_str_key = "1011" + pwm_str_key + "1"
        #print pwm_str_key
    else:
        return "Not a valid encoding"

    key_packed = bitstring.BitArray(bin=pwm_str_key).tobytes()
    return key_packed
