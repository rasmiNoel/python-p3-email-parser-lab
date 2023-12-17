import re
class EmailAddressParser:
    def __init__(self,string):
        self._string = string

    def parse(self):
        print(f'Checking {self._string} for emails...')
        regex = r"\w+([.-_]\w+)?@\w+.\w+"
        matches = re.finditer(regex,self._string)
        if(matches):
            all = []
            for match in matches:
                start,stop = match.span()
                all.insert(0,self._string[start:stop])
            return all
        else:
            print("No matches")
            return None

parse = EmailAddressParser("Hello@3.l what is matched in this?")
parse.parse()