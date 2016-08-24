# coding = utf-8
import mechanize

br = mechanize.Browser()
response = br.open("http://www.w3school.com.cn/jsref/jsref_test_regexp.asp")
html = response.read()

#print response.code
#print html

response2 = br.follow_link(text_regex="test()")
#print response2.code
#print response2.read()

br.select_form(name="tryitform")
br.form.set_all_readonly(False)
br.form['code']='123456'
br.form['bt']=''
response3 = br.submit()
content = response3.get_data()
print content
