import markdown2

def gethtml(pagename):
    html = ''
    with open(f"../entries/{pagename}.md") as f:
        for line in f:
            html += markdown2.markdown(line)
    return html
