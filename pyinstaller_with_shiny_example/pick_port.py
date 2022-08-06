import port_checker
def get_unused_port():
    starting_port = 8000
    port = starting_port
    while port_checker.is_port_in_use(port):
        port += 1
    return port
