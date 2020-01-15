"""
illustrate collection types and conversion

How can I be improved?
    DRY?
    What vs how?
    Do one thing & do it well

"""

import sys


def show_conversion(original, to):
    """ display from and to messages """

    print("from ", type(original), "\t", original)
    print("to ",  type(to), "\t", to, "\n")


def wait():
    """ version specific wait """

    message = "press Enter"
    if sys.version_info[0] < 3:
        raw_input(message)
    else:
        input(message)
    print("\n")


def main():
    """ show various examples """

    various_collections = (
                        "iuyaisuhoahsaoi",
                        ("a", "b", "c", "d"),
                        {"x","y","z"},
                        {"a": 2, "b": 3, "c": 9},
                        ["a","b","c","d"]
                        )

    print("HIGHLIGHT SOME TYPE CONVERSIONS")

    for collection in various_collections:
        print(collection, " is ",  type(collection))

        show_conversion(collection, str(collection))
        wait()
        show_conversion(collection, tuple(collection))
        wait()
        show_conversion(collection, set(collection))
        wait()


    print("DICTIONARIES ARE A BIT DIFFERENT")

    a_dict1 = various_collections[3]

    for key in a_dict1:
        print(key, a_dict1[key])

    wait()

    print("LIST COMPREHENSION")

    l = [len(collection) for collection in various_collections]
    print(l)

    wait()

    print("SET COMPREHENSION (sets remove dups)")

    s = {len(collection) for collection in various_collections}
    print(s)

    wait()

    print("GENERATOR (lazy)")
    def int_gen(n):
        for i in range(n):
            yield i
            # see also http://treyhunner.com/2018/02/python-range-is-not-an-iterator/

    ig = int_gen(30)
    next(ig)
    print(ig.__next__())
    print(ig.__next__())


if __name__ == "__main__":
    main()

