from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

encoded_ciphertext = "TXFZuhx1oB82VcoykusS4U36jkd8pbv8gofTb+lP1e35/EptuFeLnxtljyRTCy+fVa79DcLsCxcs5ChVSCSaeXnh2YgjqMzPh4cT81If9UfRiD/GFsS1Xtf5PbkBWChiEitQCbtrK4tQ6rJiLxJSrX3xBVG4YRSSUUDVm68BA6M3n86YR0A7UL5hGqwW2f3BJWF8qNOs1SM9JTD6buNGdriZ+AwsD103AoRp/2nlz4FsUS0waaRvDHmDeH27JivJToMbz+pXGLimXL0lqgZoPWt5173bpjgh4dAqvHGIaM+gfpmuZaK1IBOotXeF2exFI1CbBpbBTgTKN/YKGmJCfUxP7q817ySsd7VGcmldqonh6WComENYLqLFogS4JaWrvgBKnU6td/YmhJEszXgV6zbcln98oT+URQjlU9fHcuospeutPB/S2Z94hKbYYEbIzJNRSs4ttM3ZjqS9TqZJbkce3+vxuvC61nVd93qM8b4jw+oQ/aMTi5F/wMoAmgqbzH08cs75E2JloONyHF5Xeknz5hbRzTNvQ+YCY8KyImx8x4Dp5QpcCNTEJz546rIU5/MrexjQTVQRksS1Bpz+ONVJpBa83cKwxLJEXXa8RVJCFfravxbNT11N28wST3lcqjnK1lqvGlOfxlwE8RYaoA=="

ciphertext = base64.b64decode(encoded_ciphertext)


key = input('key: ').encode()
iv = input('iv: ').encode()

cipher = AES.new(key, AES.MODE_CBC, iv)


pt = cipher.decrypt(ciphertext)

core = unpad(pt, 16)

print(core)
