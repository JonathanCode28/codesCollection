from tkinter import *
import threading
from speedtest import Speedtest
from time import perf_counter

def run_test():
    # Disable button and show "Testing..." while running
    button.config(state=DISABLED)
    download_label.config(text="Download Speed:\nTesting...")
    upload_label.config(text="Upload Speed:\nTesting...")
    status_label.config(text="")

    def test():
        timer = perf_counter()
        try:
            st = Speedtest()
            st.get_best_server()

            download_label.config(text="Download Speed:\nMeasuring...")
            download = st.download()
            download_speed = round(download / 1e6, 2)
            download_label.config(text=f"Download Speed:\n{download_speed} Mbps")

            upload_label.config(text="Upload Speed:\nMeasuring...")
            upload = st.upload()
            upload_speed = round(upload / 1e6, 2)
            upload_label.config(text=f"Upload Speed:\n{upload_speed} Mbps")

            elapsed = round(perf_counter() - timer, 2)
            status_label.config(text=f"Done in {elapsed}s")
            print(f"Download: {download_speed} Mbps | Upload: {upload_speed} Mbps | Time: {elapsed}s")
        except Exception as e:
            status_label.config(text=f"Error: {e}")
        finally:
            button.config(state=NORMAL)

    # Run in a background thread so the UI stays responsive
    threading.Thread(target=test, daemon=True).start()


root = Tk()
root.title("SpeedTest")
root.geometry("300x400")

download_label = Label(root, text="Download Speed:\n-", font=("Arial", 14))
download_label.pack(pady=(40, 0))

upload_label = Label(root, text="Upload Speed:\n-", font=("Arial", 14))
upload_label.pack(pady=(10, 0))

status_label = Label(root, text="", font=("Arial", 10), fg="gray")
status_label.pack(pady=(10, 0))

button = Button(root, text="Click to test internet speed", font=("Arial", 12), command=run_test)
button.pack(side=BOTTOM, pady=40)

root.mainloop()