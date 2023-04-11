# NoCord

This Python script implements a simple voice chat application using the tkinter GUI toolkit, customtkinter library, socket programming, threading, and pyaudio for audio streaming. The application allows users to join a voice chat server by providing the server IP address and port number. The users can also save their usernames and chat with each other by speaking through the microphone.


## Installation


-Install Python on your system. You can download it from the official website.

-Install tkinter by running the command pip install tkinter in your command prompt or terminal.
```bash
pip install tkinter
```

-Install customtkinter by running the command pip install customtkinter in your command prompt or terminal.
```bash
pip install customtkinter
```

-Install pyaudio by running the command pip install pyaudio in your command prompt or terminal.
```bash
pip install pyaudio
```



## Usage

To start the NoCord Voice chat application, run the following command in your command prompt or terminal:
```bash
python NoCordClient.py
```
Then, launch the NoCord server as follows:
```bash
python NoCordServer.py
```

The application window will open. Enter your desired username and click on the "Save" button. Then, click on the "Join Voice Server" button and enter the server IP address and port number. Finally, click on the "Connect" button to join the voice chat.

**NOTE**: The default port for NoCordServer is 41798, you can change this in NoCordServer.py (conveniently located at the top of the script)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
