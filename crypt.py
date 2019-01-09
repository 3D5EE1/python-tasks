
from simplecrypt import decrypt, DecryptionException




passes = b'9XB8nsIqRfYeswC\n4sEhUGLEZti9BiN\nbDjmT0NcIW8nzhb\nZN6QQoMOO1ZQLUY\nRVrF2qdMpoq6Lib\ntnnX7HH3vJ9Hiji\nC24TJYYkqekv40l\nB2ropluPaMAitzE\nDRezNUVnr2zC0CP\nXCNmpTvvZb1n3mX\n'


code = b'sc\x00\x02\x96\x93^\xd7&1\x9f\xd0\x14\x02\x14\xd1\x92`\xeb\x1b\xdbulr\x0e\xeb\x0f\xf0D\xcf\x87\xf5\xd5\xf2oKA\x89b/\xaa\xa6y;\x8b)\x89\xbdl\x0f\x96\x144\x8e\xe2P\xa8\xcf\xc7T\xf6>.`m\xfbC/\xc1V\xd2>\xd0\xaf\xbb0%V\x14\xac\xf7\n\xcd'



for p in passes.split():
  try:
    s = decrypt(p, code)
  except DecryptionException:
    pass
  else:
    print(p, s)
