import re

def text_to_html(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    html_output = []
    ul_open, ol_open = False, False

    for i, line in enumerate(lines):
        # H1 sul primo paragrafo
        if i == 0 and not line.startswith(("-", "1.")):
            html_output.append(f"<h1>{line}</h1>")
            continue

        # Lista non ordinata
        if line.startswith("- "):
            if not ul_open:
                html_output.append("<ul>")
                ul_open = True
            html_output.append(f"<li>{line[2:]}</li>")
            continue
        else:
            if ul_open:
                html_output.append("</ul>")
                ul_open = False

        # Lista ordinata
        if re.match(r"^\d+\.\s", line):
            if not ol_open:
                html_output.append("<ol>")
                ol_open = True
            item = re.sub(r"^\d+\.\s", "", line)
            html_output.append(f"<li>{item}</li>")
            continue
        else:
            if ol_open:
                html_output.append("</ol>")
                ol_open = False

        # Paragrafi normali
        html_output.append(f"<p>{line}</p>")

    # Chiudo liste se rimaste aperte
    if ul_open:
        html_output.append("</ul>")
    if ol_open:
        html_output.append("</ol>")

    return "\n".join(html_output)


text = input("Inserisci qui il tuo testo: ")

html = text_to_html(text)
print(html)
