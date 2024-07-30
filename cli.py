import ollama
import click

@click.command()
@click.option("-t", help="enter the text")
def readText(t):
        if ".txt" in t:
            with open(t,'r') as input:
                response = ollama.chat(model='qwen2:0.5b', messages=[
                    {
                        'role': 'user',
                        'content': f'Summarize the content of (in lesser words) - {input.read()}',
                    },
                ])
                res = bytes(response['message']['content'],'utf-8')
                input.close()
            with open("summary.txt","wb") as output:
                output.write(res)
                output.close()
        else:
            response = ollama.chat(model='qwen2:0.5b', messages=[
                    {
                        'role': 'user',
                        'content': f'Summarize the content of (in lesser words) - {t}',
                    },
                ])
            print(response['message']['content'])

   
if __name__ == "__main__":
    readText()
