import flask
import random
app = flask.Flask(__name__)
r = random.randint(1, 10)
home = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZm50dzdheTNheXc1dHkwemZ4MjdnMm9vczByaW8yY2xqcnF4eWdiaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif"
low = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmo1enF1ZGZydG1temVudjdjMWtjeGNxcGR6bGZoemd3bWpibG9tMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UBBtgnH7afbidwQo4Q/giphy.gif"
high = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzhqdXR3cm51ZmlmemcwMWJ0dDc2cXpsYThmYnk3YmtzaGF6ZHF6ZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MXi8nBJjIBgKbyA1MM/giphy.gif"
correct = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHhyZ2xlMDUwZzR1dW03a2k0ajVieGs0NDZ3NXAwaHF3NWlsNWpzMSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l2Sq5GffrCyUMEXjW/giphy.gif"

@app.route('/')
def Main():
    return '<h1>Guess a number between 1 and 9</h1>' \
           '<img src="">'

@app.route('/<noo>')
def no(noo):
    global r
    if int(noo) < r:
        return f'<h2>Too Less.</h1><img src="{low}">'
    elif int(noo) > r:
        return f'<h2>Too High.</h1><img src="{high}">'
    elif int(noo) == r:
        r = random.randint(1, 10)
        return f'<h2>Perfect</h1><img src="{correct}">'

    return None


if __name__ == '__main__':
    app.run(debug=True)
