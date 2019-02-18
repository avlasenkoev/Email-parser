import time 
import pandas

from yellowpages import ParserYellowpages
from google_check import Google
from facebook import Facebook
from yelp import Yelp


def input():

    with pandas.ExcelFile('test_data.xlsx') as xl:
        df = xl.parse('Sheet1')

    name = df[1].tolist()
    city = df[2].tolist()
    address = df[3].tolist()
    f = lambda x, y : str(x) + ' ' + str(y)
    geo = map(f,city, address)

    data = [list(i) for i in zip(name, geo)] #list of lists
    print('input done')
    return data

def yelp_checking(data):
    start = time.time()
    try:
        yelp_close = Yelp(data).check()
        if yelp_close:
            email = 'C'
            print('C in yelp')
            return email
    except:
        pass
    end = time.time() 
    print("----{} seconds---- Yelp".format(end - start))

def fb_checking(data):
    start = time.time()
    try:
        facebook_close = Facebook(data).check()
        if facebook_close:
             email = 'C'
             print('C in fb')
             return email
        else:
            email = Facebook(data).get_mail()
            print('mail in fb!!!')
            return email
    except:
        pass 
    end = time.time() 
    print("----{} seconds---- Facebook".format(end - start))  

def g_checking(data):
    start = time.time()
    close = Google(data).check()
    if close:
        email = 'C'
        print('C in google')
        return email
    end = time.time() 
    print("----{} seconds---- Google".format(end - start))

def yellowpages(data):
    start = time.time()
    email = ParserYellowpages(data).get_email()
    end = time.time() 
    print("----{} seconds---- Yellowpages".format(end - start))
    return email

def main(data):
    start = time.time()
    counter = 0
    for item in data:
        if g_checking(item) == 'C':
            email = 'C'
            item.append(email)
            continue
        if yelp_checking(item) == 'C':
            email = 'C'
            item.append(email)
            continue
        if fb_checking(item) == 'C':
            email = 'C'
            item.append(email)
            continue
        if fb_checking(item) != None:
            email = fb_checking(item)
            item.append(email)
            continue
        if yellowpages(item) != None:
            email = yellowpages(item)
            item.append(email)
            print('mail in yellowpages!!!')
            continue
        item.append('')

        counter += 1
        print(counter, 'uups, empty =(')
    end = time.time() 
    print("----{} seconds---- All".format(end - start))
    return data

def to_exel(data):
    email_data = pandas.DataFrame(
        data,
        columns=['Name', 'Address', 'Mail']
        )
    with pandas.ExcelWriter('emails.xlsx') as xl:
        email_data.to_excel(writer, "Sheet1")
        writer.save()
    print('export finished, well done!!!')

if __name__ == '__main__':
    input_data = input()
    output_data = main(input_data)
    to_exel(output_data)



