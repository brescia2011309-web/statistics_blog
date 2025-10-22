#!/usr/bin/env python3
"""
rsa_demo.py

Simple demo: read the hidden passage inside homework2.html, normalize to a-z,
encode as 2-letter base-26 blocks, encrypt with small RSA (p=61,q=53,e=17),
then factor n to recover the private key and decrypt. Finally compute letter
frequencies and a chi-squared score against a small Italian frequency profile.

This script is intentionally educational and uses tiny primes — do NOT use
this for any real security purpose.
"""
import re
from collections import Counter
import math


def read_passage_from_html(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.search(r"<script[^>]*id=[\"']passage[\"'][^>]*>(.*?)</script>", text, re.S)
    if not m:
        raise SystemExit('passage script block not found in html')
    return m.group(1).strip()


def normalize(text):
    import unicodedata
    s = unicodedata.normalize('NFKD', text)
    # remove diacritics
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    s = s.lower()
    # keep only a-z
    s = re.sub('[^a-z]', '', s)
    return s


def encode_pairs(s):
    # map two letters to a number: a->0..z->25; value = 26*x + y
    if len(s) % 2 == 1:
        s += 'x'  # padding
    blocks = []
    for i in range(0, len(s), 2):
        x = ord(s[i]) - 97
        y = ord(s[i+1]) - 97
        blocks.append(x * 26 + y)
    return blocks


def decode_pairs(blocks):
    chars = []
    for v in blocks:
        x = v // 26
        y = v % 26
        chars.append(chr(x + 97))
        chars.append(chr(y + 97))
    return ''.join(chars)


def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m


def factor_small(n):
    # trial divide to find small prime factors (suitable for this demo)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None


def letter_freq(s):
    c = Counter(s)
    n = sum(c.values()) or 1
    return {ch: c.get(ch, 0) / n for ch in 'abcdefghijklmnopqrstuvwxyz'}


def chi_squared(obs_freq, exp_freq):
    # chi-squared over 26 letters
    s = 0.0
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        o = obs_freq.get(ch, 0)
        e = exp_freq.get(ch, 1e-6)
        s += (o - e) ** 2 / (e if e > 0 else 1e-6)
    return s


def main():
    html_path = 'homework2.html'
    raw = read_passage_from_html(html_path)
    norm = normalize(raw)
    print('\nNormalized text (first 200 chars):')
    print(norm[:200] + ('...' if len(norm) > 200 else ''))

    blocks = encode_pairs(norm)
    print(f'\nNumber of 2-letter blocks: {len(blocks)}')

    # small primes (educational only)
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = modinv(e, phi)

    print('\nRSA parameters (small, demo only):')
    print(f' p={p}, q={q}, n={n}, e={e}, d={d}')

    # encrypt
    cipher = [pow(m, e, n) for m in blocks]
    print('\nCiphertext blocks (first 40):')
    print(cipher[:40])

    # attacker factors n (easy here) and recovers d
    factors = factor_small(n)
    if factors:
        fp, fq = factors
        print(f'\nFactored n: p1={fp}, p2={fq}')
        phi_att = (fp - 1) * (fq - 1)
        d_att = modinv(e, phi_att)
        # decrypt
        plain_blocks = [pow(c, d_att, n) for c in cipher]
        recovered = decode_pairs(plain_blocks)
        print('\nRecovered normalized plaintext (first 200 chars):')
        print(recovered[:200] + ('...' if len(recovered) > 200 else ''))

        # compare letter frequencies vs expected Italian frequencies (approx.)
        # approximate Italian letter frequencies (normalized): source: rough estimates
        italian_expected = {
            'a':0.117, 'b':0.012, 'c':0.049, 'd':0.037, 'e':0.118, 'f':0.01,
            'g':0.017, 'h':0.007, 'i':0.106, 'j':0.0001,'k':0.0001,'l':0.065,
            'm':0.025, 'n':0.067, 'o':0.098, 'p':0.035, 'q':0.009, 'r':0.063,
            's':0.049, 't':0.056, 'u':0.031, 'v':0.023, 'w':0.0001,'x':0.0001,
            'y':0.0001,'z':0.012
        }

        obs = letter_freq(recovered)
        chi2 = chi_squared(obs, italian_expected)
        print(f'\nChi-squared vs Italian expected frequencies: {chi2:.4f}')
    else:
        print('Could not factor n (unexpected for these small primes)')


if __name__ == '__main__':
    main()
