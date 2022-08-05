import subprocess
import webbrowser
cmd = ['shiny', 'run', 'my_app/app.py']


def run():
    p = subprocess.Popen(
                        cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
    url = 'http://localhost:8000'
    webbrowser.open(url, new=0, autoraise=True)
    # For debugging
    for line in iter(p.stdout.readline, b''):
        print(f">>> {line.rstrip().decode('utf-8')}")
        if "connection closed" in line.rstrip().decode('utf-8'):
            p.kill()