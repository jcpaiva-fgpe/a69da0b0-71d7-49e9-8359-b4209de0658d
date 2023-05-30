def rgb_to_hex(r, g, b):
    r_hex = hex(r)[2:].rjust(2, '0')
    g_hex = hex(g)[2:].rjust(2, '0')
    b_hex = hex(b)[2:].rjust(2, '0')
    return r_hex+g_hex+b_hex