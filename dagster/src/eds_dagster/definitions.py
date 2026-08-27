import dagster as dg


@dg.asset
def eds_test():
    return "EDS OK"


defs = dg.Definitions(
    assets=[eds_test],
)
