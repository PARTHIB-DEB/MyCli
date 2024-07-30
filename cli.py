import ollama
import click


@click.command()
@click.option("-t", help="enter the text")
def commandline(t):
    """
    Takes either a (.txt) file or a textual paragraph as argument
    """
    if ".txt" in t:  # Check whether .txt is in the argument

        with open(t, "r") as input:  # Open the .txt file to read in texual mode
            response = ollama.chat(
                model="qwen2:0.5b",
                messages=[
                    {
                        "role": "user",
                        "content": f"Summarize the content of (in lesser words) - {input.read()}",
                    },
                ],
            )
            res = bytes(response["message"]["content"], "utf-8")  # Convert the textual string into binary string or array of bytes
            input.close()

        with open("summary.txt", "wb") as output:  # Open the summary.txt file in write mode for binary strings
            output.write(res)
            output.close()
    else:

        response = ollama.chat(
            model="qwen2:0.5b",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the content of (in lesser words) - {t}",  # Send the raw textual argument to Model
                },
            ],
        )

        res = response["message"]["content"]
        print(f"\n\n\t{res}\t\n\n")  # Paste the textual output in shell


if __name__ == "__main__":
    commandline()
