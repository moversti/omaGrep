import re
import os
import argparse
import tkinter as t


# TODO: Scrollipalkit resultseihin

def _greppaa(patt, fram):
    lorem_pattern = re.compile(patt, re.IGNORECASE)
    for scan in os.scandir():
        if scan.is_file():
            f = t.LabelFrame(fram)
            f.pack(anchor='nw', fill='both')
            tied = open(scan.name, 'r')
            linenro = 1
            for line in tied.readlines():
                s = lorem_pattern.search(line)
                if s:
                    text = scan.name + ':' + str(linenro) + ': ' + line
                    lab = t.Label(f, text=text)
                    lab.pack(anchor='w')
                linenro += 1
            tied.close()


def clear_ja_greppaa(patt, fram):
    # TODO: clearaa vanhat resultsit
    _greppaa(patt, fram)


parser = argparse.ArgumentParser()
parser.add_argument('pattern')
args = parser.parse_args()
root = t.Tk()
ent = t.Entry(root)
ent.insert(0, args.pattern)
ent.pack()
nappi = t.Button(root, text='HAE', command=lambda: clear_ja_greppaa(ent.get(), root))
nappi.pack()
# _greppaa(args.pattern, root)

root.iconify()
root.update()
root.deiconify()
root.mainloop()
