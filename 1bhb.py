text = 'This is 1st line\nThis is 2nd line\nThis is 3rd line\n'
fp = open('foo.txt', 'w+')
fp.write(text)
# 51

# >>> fp.tell()
# # 51
#
# >>> fp.seek(0)
# # 0
# >>> fp.read(10)
# # 'This is 1s'
#
# >>> fp.tell()
# # 10
# >>> fp.read(15)
# # 't line\nThis is '
#
# >>> fp.tell()
# # 25
#
# >>> fp.close()