# hchat
HChat is an experimental project for automated language translated chatbots 

## Installation

### Installing Rasa is easy
```
pip install rasa
```

### Installing Rasa X
Details can be found here: https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide
```
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
```

## Training
Inside the /cn or /en directories issue the following command:
```
rasa train
```

## Running the servers

We need to run the chat bot as well as the action server for retrieving weather info.

### Running the chatbot
Inside the /cn or /en directories
```
rasa run --enable-api --cors "*" --port 5004 --debug
```
## Running the action server
Inside the /cn or /en directories
```
rasa run actions --port 5055 --debug
```