"""

给你一个字符串 s 和一个整数 t，表示要执行的 转换 次数。每次 转换 需要根据以下规则替换字符串 s 中的每个字符：

如果字符是 'z'，则将其替换为字符串 "ab"。
否则，将其替换为字母表中的下一个字符。例如，'a' 替换为 'b'，'b' 替换为 'c'，依此类推。
返回 恰好 执行 t 次转换后得到的字符串的 长度。

由于答案可能非常大，返回其对 109 + 7 取余的结果。


输入： s = "abcyy", t = 2
输出： 7

"""

from collections import defaultdict


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        _tmp = defaultdict(int)

        for ch in s:
            _tmp[ch] += 1

        # print(_tmp)

        for _ in range(t):
            _action = defaultdict(int)

            for ch in _tmp:
                if ch == 'z':
                    _action['a'] += _tmp[ch]
                    _action['b'] += _tmp[ch]
                else:
                    _action[chr(ord(ch) + 1)] += _tmp[ch]
                _action[ch] -= _tmp[ch]

            for k, v in _action.items():
                _tmp[k] += v

            # print(_tmp)

        return sum(_tmp.values()) % (10 ** 9 + 7)


class Solution2:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        ans = len(s)

        _tmp = [0 for _ in range(26)]
        for ch in s:
            _tmp[ord(ch) - ord('a')] += 1

        for _ in range(t):
            cnt_z = _tmp[-1]
            ans += cnt_z

            # list element option
            for i in range(25, 1, -1):
                _tmp[i] = _tmp[i - 1]
            _tmp[1] = _tmp[0] + cnt_z
            _tmp[0] = cnt_z

        return ans % (10 ** 9 + 7)


if __name__ == '__main__':
    ret = Solution2().lengthAfterTransformations('abcyy', 2)
    print(ret)

    s = ("rssjmowborzlmeqqqobyqcejqloqicrzuioahtgvdfptpdiofq"
         "nnximowhqovyqxhclnokkvqjwsrftkyerwnbecbmanninbgwwk"
         "glezhocqjwgzlqddzojmiohtkqdrmjiowbfvtzrqtzmkcfmivd"
         "iqqqueacibannstgtvqsijncxchwbfdvmqlzfinhijodevmabk"
         "cubwzwhyytfbveefesyayesszwgmzyurpzyjohvywngbtokweq"
         "ujxcjyoeyoarnlopivfuenhzounucgeuawoxgqvixmlpjmqbvm"
         "tunksququawvbmwzyftijgkmkzxhqjleoblkyfdcycsnzvriyg"
         "ckuaxwendcmgfbrnggsozmhxmdpiuuopgfnxekoyfnlhzctdkf"
         "dwzbrdjxrvqqnasaqvtdrcqcgfdmpxakujbsrmcintncablupx"
         "htzsqivaetfcufmxsmugzzmkhlachvgemgwrrhevzzpsqjvhgy"
         "alfpnxbfxhyglxfhfvbpbypyourftcowtnsykcadbqufdzihzs"
         "jylccmjohjajyejuwnosiovynbosxewxhksoszumnfmapjuvkm"
         "enmtanjbrldmfrlvoofdtluktbwwzavxxsbcrsvpbzbpqdutas"
         "uiowhmtgowvghndncmhrusxgfrjrcrqwrvtlvpxdfydeqyzowx"
         "xgrpgrzrotpaxhcrrpoeuomoxklvgdfdnhbgwpolpwfuscyvlk"
         "pbamwcbmqoofplzevjkspktcjanfglhygtfbqxagnqtpgfhpkq"
         "gnywzvckdbbyfmyklxpwqsslctqerxgxwumoxvetprjrmttxdj"
         "yarbjucsaanhmxknqlnanqzmzearndgslboqubuxmvhwcrnqhu"
         "oiebalcsaektkbzwztkaluhecfpwvzdzjyfzevxroclrdqwlxj"
         "xuadsntsbidptxrlwjyzubzflxllsntjcbxexciujwcqbljist"
         "pyaepabpophyhxhzfgbavxwsaodglknjgnbqspreylgaiziqzh"
         "yeafdubhvtfgflkcgwhsocjhywnqjvqqwxdoymzfskibejnwar"
         "qpjyootzvqfgqzavutozkzebfvbagtsgpkreraifogvyaxjruk"
         "cxnwurpnpmmyqcsegkiakepsvxgpillpzsuonmixasdjbpzmbl"
         "kgjaiwmlmqoxaameqrcawskfqsjccxeqlwuxczhtxwgcojiofq"
         "kttffaflpuihwpg")

    ret = Solution2().lengthAfterTransformations(s, 3434)
    print(ret)
