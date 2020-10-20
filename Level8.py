import codecs
import bz2


usrStr=R'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'


print(bz2.decompress(codecs.escape_decode(usrStr)[0]))


# un:huge
# ps:file