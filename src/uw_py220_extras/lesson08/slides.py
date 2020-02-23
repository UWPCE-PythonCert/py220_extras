"""
make it really easy to create a markdown presentation
illustrates functional approach
"""
import fileinput


def help():
    print("-Slide,*Bullets,`Code delimit, .Image,")


def grab_input(exit_cmd="x"):
    grabbed = []
    for line in fileinput.input():
        line = line.strip()
        if line == exit_cmd:
            return grabbed
        grabbed += (line,)


def transform(originals, replacements):
    transformed = []
    for original in originals:
        substitute = replacements.get(original)
        if substitute is not None:
            transformed += (substitute,)
        else:
            transformed += (original,)
    return transformed


def write(content):
    for line in content:
        print(line)


if __name__ == "__main__":

    substitutions = {
        "-": "---",
        ".": "<img=kjhkjhkj>",
        "`": "```"
    }

    help()
    raw_content = grab_input()

    slide_content = transform(raw_content, substitutions)
    write(slide_content)
