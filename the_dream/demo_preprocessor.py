# Author: Lachlan Whyborn
# Last Modified: Thu 10 Oct 2024 14:55:16

ProcessingFunctions = {
        "read": ReadDataset,
        "sum-of-squares": SumOfSquares,
        "swinbank": Swinbank
}

def ReadDataset(Config):
    """Read a set of NetCDF files as an xarray MFdataset."""

def SumOfSquares(Config):
    """Compute the magnitude of a vector described by the inputs."""

def Swinbank(Config):
    """Perform the Swinbank calculation on SWdown."""

def ProcessVariable(VarName, Config):

    # Perform derivation
    Data = ProcessingFunctions[Config["function"]](Config["inputs"])

    ScaleData(Data, Config["scale"])

    MakeCFCompliant(VarName, Data)

    WriteToDisk(Data)

if __name__ == "__main__":

    # Read the yaml, then pass outcomes
    with open("config.yaml", "r") as cfg_f:
        cfg = yaml.safe_load(cfg_f)

    for var, var_config in cfg.items:
        ProcessVariable(var, var_config)
