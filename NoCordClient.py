import tkinter as tk
import customtkinter as ct
import socket
import threading
import pyaudio

# Audio streaming parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# PyAudio Object
audio = pyaudio.PyAudio()

# Audio stream object
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK)

# Play audio functionality
def play_audio(client_socket):
    while True:
        try:
            # Receiving audio from client
            data = client_socket.recv(1024)
            stream.write(data)
        except:
            # If there is an error, we stop the audio.
            break

def join_chat():
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server host name + port
    host_label = ct.CTkLabel(app, text='Host IP:')
    host_label.pack(padx=10, pady=10)
    host_entry = ct.CTkEntry(app)
    host_entry.pack()
    port_label = ct.CTkLabel(app, text='Enter the port (default is 41798)')
    port_label.pack(padx=10, pady=10)
    port_entry = ct.CTkEntry(app)
    port_entry.pack()

    def connect():
        host = host_entry.get()
        port = int(port_entry.get())
        client_socket.connect((host, port))
        connectedclient = ct.CTkLabel(app, text='Connected to the server!')
        connectedclient.pack(padx=10, pady=10)
        useradd = user_var.get()
        client_socket.sendall(useradd.encode('utf-8'))
        audio_thread = threading.Thread(target=play_audio, args=(client_socket,))
        audio_thread.start()
        port_label.forget()
        port_entry.forget()
        host_label.forget()
        host_entry.forget()
        connect_button.forget()

        # Communication thread
        def comm_thread():
            while True:
                try:
                    data = stream.read(CHUNK)
                    client_socket.sendall(data)
                except:
                    break

            client_socket.close()
            stream.stop_stream()
            stream.close()
            audio.terminate()

        comm_thread = threading.Thread(target=comm_thread)
        comm_thread.start()

    connect_button = ct.CTkButton(app, text='Connect', command=connect)
    connect_button.pack(padx=10, pady=10)



def save_username():
    # Hide input box and save button
    user.pack_forget()
    save_user.pack_forget()

    # Update label with user name
    username_text = f'Welcome, {user_var.get()}!'
    username.configure(text=username_text)
    username.pack(padx=10, pady=10)


# UI Settings
ct.set_appearance_mode('System')
ct.set_default_color_theme('green')

# App frame
app = ct.CTk()
app.geometry('800x600')
app.title('NoCord Voice')


# UI Elements
title = ct.CTkLabel(app, text='NoCord Voice')
title.pack(padx=10, pady=10)

# User input for Username
username = ct.CTkLabel(app, text='Enter your Username: ')
username.pack(padx=10, pady=10)
user_var = tk.StringVar()
user = ct.CTkEntry(app, width=200, height=40, textvariable=user_var)
user.pack()
save_user = ct.CTkButton(app, text='Save', command=save_username)
save_user.pack(padx=10, pady=10)

# Joining button
join = ct.CTkButton(app, text='Join Voice Server', command=join_chat)
join.pack(padx=1, pady=1)



app.mainloop()
