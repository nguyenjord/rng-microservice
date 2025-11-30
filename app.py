import zmq, json, random


def gen_rand(min, max):
    return random.randint(min, max)

def gen_rand_list(min, max, count):
    return [random.randint(min, max) for _ in range(count)]

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:4000")
    print("Random number generator microservice running on port 4000")

    while True:
        message = socket.recv_string()
        request = json.loads(message)

        method = request.get("method")
        params = request.get("params",{})

        if method == "rand":
            response = gen_rand(params["min"],params["max"])

        elif method == "rand_list":
            response = gen_rand_list(params["min"], params["max"], params["count"])
        else:
            response = {"error": "Unknown value"}

        socket.send_string(json.dumps(response))

if __name__ == "__main__":
    main()