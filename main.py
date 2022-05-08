import yaml

template_start = '<!DOCTYPE html><html lang="en"><head> <meta charset="UTF-8"> <meta http-equiv="content-type" ' \
                 'content="text/html; charset=UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta ' \
                 'name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"> ' \
                 '<title>Navigation</title> <style> @import url(' \
                 'https://necolas.github.io/normalize.css/latest/normalize.css); @import url(' \
                 'https://cdn.jsdelivr.net/npm/firacode@6.2.0/distr/fira_code.css); body { font-family: "Fira Code", ' \
                 'monospace; background-color: #2e2e2e; color: #d6d6d6; display: flex; justify-content: space-around; ' \
                 '} @supports (font-variation-settings: normal) { body { font-family: "Fira Code VF", monospace; } } ' \
                 '.column { display: flex; flex-direction: column; width: 25%; text-align: center; } .row { ' \
                 'margin-bottom: 4px; height: 2em; } h2 { font-size: 2em; } a { text-decoration: none; color: ' \
                 '#d6d6d6; transition-duration: 0.5s; font-size: 2em; } a:hover { scale: 1.2; } @media (max-width: ' \
                 '800px) { body { flex-direction: column; justify-content: space-around; } .row { height: auto; } ' \
                 '.column { width: 100%; } } </style></head><body> '

template_end = '</body></html>'

with open('navigation.yml', 'r') as f:
    html = ""
    doc = yaml.load(f, Loader=yaml.FullLoader)
    for title in doc['titles']:
        title = title['title']
        html = html + f'''<div class="column"><h2>{title['name']}</h2>'''
        items = title['items']
        if doc['sorted']:
            items = sorted(items, key=lambda x: len(x['name']), reverse=True)

        for item in items:
            html = html + f'''<a class="row" href="{item['url']}"><p>{item['logo']} {item['name']}</p></a>'''
        html = html + '</div>'
    print(template_start + html + template_end)
