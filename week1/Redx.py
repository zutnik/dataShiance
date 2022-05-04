import re



#
#
# def names():
#     simple_string = """Amy is 5 years old, and her sister Mary is 2 years old.
#     Ruth and Peter, their parents, have 3 kids."""
#     x = re.findall("[A-Z]+[a-z]*[\w]", simple_string)
#     return len(x)
#

# names()


def grades():
    with open("../../dataShiance/assignments/assignment1/assets/grades.txt", "r") as file:
        grades = file.read()
        result = []
        for item in re.finditer("(?P<name>.*)+(\: B)",grades):
            result.append(item.group('name'))
        return result
    # YOUR CODE HERE


#  raise NotImplementedError()
grades()
print(grades()[0])

# def logs():
#     with open("../assignments/assignment1/assets/logdata.txt", "r") as file:
#         logdata = file.read()
#         for item in re.finditer("(?P<host>\d*\.\d*\.\d*\.\d*) - (?P<user_name>-|[\w]+) \[(?P<time>\w{2}/\w*/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})\] \"(?P<request>\D*?/?\D*?/?\D*?/?\D*?/?\D* \w+/\d*\.\d*)\"", logdata):
#             print(item.groupdict())
#         return item
#
#
# logs()
# print(len(logs()))
# def logs():
#     with open("../assignments/assignment1/assets/logdata.txt", "r") as file:
#         logdataBogdan = file.read()
#         logsBogdan = []
#         pattent = """
#         (?P<host>.*)
#         (\ -\ )
#         (?P<user_name>.*)
#         (\ \[)
#         (?P<time>.*)
#         (\]\ \")
#         (?P<request>.*)
#         (\")
#         """
#         for item in re.finditer(pattent, logdataBogdan,re.VERBOSE):
#             logsBogdan.append(item.groupdict())
#         return logsBogdan
#
#
# logs()
# print(logs()[0])

# YOUR CODE HERE
# raise NotImplementedError()
# #%%
# assert len(logs()) == 979
#
# one_item = {'host': '146.204.224.152',
#             'user_name': 'feest6811',
#             'time': '21/Jun/2019:15:45:24 -0700',
#             'request': 'POST /incentivize HTTP/1.1'}
# assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"
