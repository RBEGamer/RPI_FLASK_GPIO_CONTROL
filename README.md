# super-duper-flask-led-pi-thing
A short demo for IT2 Lesson; How to use Flask to light up LEDs on a PI


# REDIRECT TO INDEX.html
```python

@app.route('/')
def index_redirect():
    return redirect("/static/index.html", code=302)
```
