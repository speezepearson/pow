#!/usr/bin/python

'''The core of PRPG's algorithm.

This algorithm (and the salt, and your master password) is all you need in order to recompute a password. The rest of this package is just a nice UI to this module.
'''

import hashlib
from typing import Sequence

def number_to_password(n: int, charsets: Sequence[str]) -> str:
  result = ''
  for charset in reversed(charsets):
    (n, i) = divmod(n, len(charset))
    result = charset[i] + result

  charset = ''.join(charsets)
  while n > 0:
    (n, i) = divmod(n, len(charset))
    result = charset[i] + result

  return result

def master_and_salt_to_password(master: str, salt: str, charsets: Sequence[str]) -> str:
  key = hashlib.pbkdf2_hmac(
          hash_name='sha256',
          password=master.encode('utf-8'),
          salt=salt.encode('utf-8'),
          iterations=10**6)
  sha = hashlib.sha256(key).hexdigest()
  n = int(sha, 16)
  return number_to_password(n, charsets)
