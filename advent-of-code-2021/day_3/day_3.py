import collections


def part_1(bytes):
    gamma, epsilon = "", ""
    for i in range(len(bytes[0])):
        c = collections.Counter([byte[i] for byte in bytes]).most_common()
        gamma += c[0][0]
        epsilon += c[-1][0]
    return int(gamma, 2) * int(epsilon, 2)


def part_2(bytes):
    diag = {
        "oxy_bytes": [1, bytes],
        "co2_bytes": [0, bytes],
    }
    for i in range(len(bytes[0])):
        for k, (typ, bytes) in diag.items():
            if len(bytes) > 1:
                c = collections.Counter([byte[i] for byte in bytes]).most_common()
                if c[0][1] != c[-1][1]:
                    keep = c[typ - 1][0]
                else:
                    keep = str(typ)
                diag[k][1] = [b for b in bytes if b[i] == keep]
    oxy_rating = int(diag["oxy_bytes"][1][0], 2)
    co2_rating = int(diag["co2_bytes"][1][0], 2)
    return oxy_rating * co2_rating
