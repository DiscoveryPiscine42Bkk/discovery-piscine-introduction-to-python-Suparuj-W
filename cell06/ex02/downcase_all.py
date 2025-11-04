import sys

def downcase_it(text):
    return text.lower()

params = sys.argv[1:]
if not params:
    print("none")
else:
    for p in params:
        print(downcase_it(p))