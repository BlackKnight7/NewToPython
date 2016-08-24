import mechanize

br = mechanize.Browser()
response = br.open("http://www.w3school.com.cn/jsref/jsref_test_regexp.asp")
html = response.read()

print response.code
print html
