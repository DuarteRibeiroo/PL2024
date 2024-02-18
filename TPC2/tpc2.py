import re
import sys

def main():
    header_exp = re.compile(r'^#\s(.*)')
    subheader_exp = re.compile(r'^##\s(.*)')
    subsubheader_exp = re.compile(r'^###\s(.*)')
    bold_exp = re.compile(r'\*\*(.*)\*\*|__(.*)__')
    italic_exp = re.compile(r'\*(.*)\*|_(.*)_')
    link_exp = re.compile(r'[^!]\[(.*)\]\((.*)\)')
    img_exp = re.compile(r'!\[(.*)\]\((.*)\)')
    numbered_list_exp = re.compile(r'^\d+\.\s(.*)')
    in_numbered_list = False
    for line in sys.stdin:
        #remove \r (windows user)
        line = line.rstrip()
        line = header_exp.sub(r'<h1>\1</h1>',line)
        line = subheader_exp.sub(r'<h2>\1</h2>',line)
        line = subsubheader_exp.sub(r'<h3>\1</h3>',line)
        line = bold_exp.sub(r'<b>\1\2</b>',line)
        line = italic_exp.sub(r'<i>\1\2</i>',line)
        line = link_exp.sub(r'<a href="\2">\1</a>',line)
        line = img_exp.sub(r'<img src="\2" alt="\1"/>',line)
        
        subs = numbered_list_exp.subn(r'<li>\1</li>',line)
        if in_numbered_list:
            #Exit "numbered list mode"
            if subs[1] == 0:
                in_numbered_list = False
                print(r'</ol>')
            else:
                line = "    " + subs[0]
        else:
            #Enter "numbered list mode"
            if subs[1] != 0:
                in_numbered_list = True
                print(r'<ol>')
                line = "    " + subs[0]
        print(line)
    
if __name__ == "__main__":
    main()