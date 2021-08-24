import re

text = """
Giraffes have aroused
the curiosity of __PLURAL_NOUN__
since eraliest times. The
giraffe is the tallest of all
living __PLURAL_NOUN__, but
scientists are unable to
explain how it got its long
__PART_OF_THE_BODY__. The
giraffe's tremendous height,
which might reach __NUMBER__
__PLURAL_NOUN__, comes from
its legs and __BODYPART__.
"""
def mad_libs(mls):
    """
    :param mls: String with parts the user should fill out surrounded by double underscores.
    Underscores cannot be inside hint e-g-, no __hint_hint__ only __hint__.
    """

    hints = re.findall("__.*?__", mls)

    if hints is not None:
        for word in hints:
            q = "Enter a {}: ".format(word)
            new = input(q)
            mls=mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", " ")
        print(mls)
    else:
        print("Invalid mls")

mad_libs(text)

"""
Here we find all instances of double underscores ind the text and use it to hint
what kind of word the player should enter.
Then we replace all hints with the entered words and print the mad lib again.
We have btw removed new lines in the mad lib and replaced them with a space
"""
