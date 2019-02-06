from yellowpages import ParserYellowpages
from input_data import data
from output_data import to_exel

for item in data:
    parser_object = ParserYellowpages(item)
    email = parser_object.get_email()
    if email is None:
        email = ''
    item.append(email)

to_exel(data)
