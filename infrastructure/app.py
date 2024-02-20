from aws_cdk import App
from config import build_app_config
from pgStacInfra import pgStacInfraStack
from vpc import VpcStack

pgStacInfra = App()

app_config = build_app_config()

vpc_stack = VpcStack(scope=pgStacInfra, app_config=app_config)

pgstac_infra_stack = pgStacInfraStack(
    scope=pgStacInfra,
    vpc=vpc_stack.vpc,
    app_config=app_config,
)
pgStacInfra.synth()
