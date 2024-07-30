import click
import ollama

@click.group()
def cli():
    pass

@click.command()
@click.option("-t", help="enter the text")
def commandline(t):
    if ".txt" in t:
        
        res = summary_response(t)
        with open("output.txt","wb") as output:
            output.writelines(res)
            res.close()
            output.close()
        
    else:
        click.echo(f"\n\n\t Summary - {t}\t\n\n")

def summary_response(file):
    # with open(file,"r") as ip:
    #     data=ip.read().replace("\n"," ")
    #     print(data)
    #     ip.close()
    # input = open(file,"rb")
    # return input
    pass

cli.add_command(commandline)

if __name__ == "__main__":
    cli()
