from flask import Flask, Blueprint, render_template, request

app = Flask(__name__)

def filter_content(ctx):
    include_title = request.args.get('include_title')
    include_description = request.args.get('include_description')
    exclude_title = request.args.get('exclude_title')
    exclude_description = request.args.get('exclude_description')
    limit = request.args.get('limit', type=int)
    items = ctx['items'].copy()
    items = [item for item in items if include_title in item['title']] if include_title else items
    items = [item for item in items if include_description in item['description']] if include_description else items
    items = [item for item in items if exclude_title not in item['title']] if exclude_title else items
    items = [item for item in items if exclude_description not in item['description']] if exclude_description else items
    items = items[:limit] if limit else items
    ctx = ctx.copy()
    ctx['items'] = items
    return ctx

@app.route("/filter")
def rss_filter():
    from filter import ctx
    feed_url = request.args.get("feed")  
    return render_template('atom.xml', **filter_content(ctx(feed_url)))

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=9000)
