import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    """Group with two subcommands generating the sin en tan of x values from 0 to 2 pi, with the option to choose the number of x values between 0 and 2 pi.
    """
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=1,
    type=int)
def sin(number):
    """Generating the sinus between 0 and 2 pi  and printing the dataframe of x from 0 to 2 pi and its corresponding sin.

    Args:
        number (int): Number of x values between 0 and 2 pi

    Return: none 
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 2,
    type = int)
def tan(number):
    """Generating the tangens from 0 to 2 pi and printing the dataframe of x from 0 to 2 pi and its corresponding tan. 

    Args:
        number (int): Number of x values between 0 and 2 pi 

    Return: none
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return 


if __name__ == "__main__":
    cmd_group()