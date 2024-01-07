import threading
import flask_server
import osc_server
import osc_sender

if __name__ == "__main__":
    try:
        flask_server = threading.Thread(target=flask_server.run_flask)
        flask_server.start()

        osc_server = threading.Thread(target=osc_server.run_server)
        osc_server.start()

        osc_sender = threading.Thread(target=osc_sender.interval_get_initial_data)
        osc_sender.start()
        
    except KeyboardInterrupt:
        print("Shutting down")
    else:
        flask_server.join()
        osc_server.join()
        osc_sender.join()
