# MyCli

## Installation

- Install & Setup Ollama in respective operating systems from the github repository : [link](https://github.com/ollama/ollama)

- Setup for any linux distros : [link](https://github.com/ollama/ollama/blob/main/docs/linux.md)

### Environment Setup
- Create a Virtualenv ```venv```
```bash
python3 -m venv venv
```
- Activate Virtualenv ```venv``` (Linux)
```bash
source venv/bin/activate
```

### Libraries
- Click (8.1.7)
- Ollama (Model - qwen2:0.5b)
- Ruff (0.5.5)

```bash
pip install click ollama ruff
```
Or you can follow these steps -

- Clone the repository

```bash
git clone https://github.com/PARTHIB-DEB/Bayesian-Technologies.git
```

- Install all libraries from **requirements.txt**

```bash
pip install -r requirements.txt
```

## Run and Input-Output

### Ollama Server
- Start the Ollama server
```bash
sudo systemctl start ollama
```
- Check whether you can run qwen2:0.5b model in shell
```bash
ollama run qwen2:0.5b
```

### Script (cli.py)

The *cli.py* script has only one function - *commandline()* . This function takes parameter **-t** and an argument which is either a text file (e.g: **book.txt**) or any paragraphs. While giving a paragraph as an argument , either seperate each word with a specifier or enclose the whole string within single or double quotes or some brackets.

- Run the cli application by passing **text file**
```bash
python cli.py -t book.txt
```
This command will generate the summary as output and store it into a specific file - **summary.txt**


- Run the cli application by passing **textual paragraphs**
```bash
python cli.py -t "The quick brown fox jumped over the lazy dog"
```

This command will generate the summary as output and paste it on the shell


## Challenges
Its my first time to make a cli using python . So I faced couple small challenges which I have stated below - 
- **Setup Ollama** - Didn't know about how to install and setup Ollama in my Fedora OS. I just installed the python library in the project but when the time came to test the connection , I faced *httpx.connectionRefused* error. Then I realised that I have to configure it in my local environment

- **binary to text** - Python's IO library is used for handling all file related operation. Its already within the default python packages. I thought the summary response from qwen2:0.5b model can be directly written into *summary.txt* but I was proved wrong. So I changed the response into Binary format or bytes format , so that I can write the output in the *summary.txt*

## Suggestions
Although it's a very small cli application , yet it can be improved. As we know , the text file (*book.txt* here) is within the same path of the project but it can be in any other location. So , the functionality of using a text-file in any distant path can be applied in the *cli.py* in future.
