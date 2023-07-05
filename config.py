from typing import Any, Dict, List, Optional, Union

import pydantic
from aws_cdk import aws_ec2


class Config(pydantic.BaseSettings):
    project_id: Optional[str] = pydantic.Field(
        description="Project ID", default="cdk-eoapi-demo"
    )
    stage: Optional[str] = pydantic.Field(
        description="Stage of deployment", default="test"
    )
    auth_provider_jwks_url: Optional[str] = pydantic.Field(
        description="""Auth Provider JSON Web Key Set URL for
        ingestion authentication. If not provided, 
        no authentication will be required."""
    )
    data_access_role_arn: Optional[str] = pydantic.Field(
        description="Role ARN for data access, if none will be created at runtime.",
    )
    db_instance_type: Optional[str] = pydantic.Field(
        description="Database instance type", default="t3.micro"
    )
    db_allocated_storage: Optional[int] = pydantic.Field(
        description="Allocated storage for the database", default=5
    )
    public_db_subnet: Optional[bool] = pydantic.Field(
        description="Whether to put the database in a public", default=False
    )
    nat_gateway_count: Optional[int] = pydantic.Field(
        description="Number of NAT gateways to create", default=1
    )
    bastion_host_create_elastic_ip: Optional[bool] = pydantic.Field(
        description="Whether to create an elastic IP for the bastion host",
        default=False,
    )
    bastion_host_allow_ip_list: Optional[List[str]] = pydantic.Field(
        description="""YAML file containing list of IP addresses to 
        allow SSH access to the bastion host""",
        default=[],
    )
    bastion_host_user_data: Optional[
        Union[Dict[str, Any], aws_ec2.UserData]
    ] = pydantic.Field(
        description="Path to file containing user data for the bastion host",
        default=aws_ec2.UserData.for_linux(),
    )
    titiler_buckets: Optional[List[str]] = pydantic.Field(
        description="""Path to YAML file containing list of
        buckets to grant access to the titiler API""",
        default=[],
    )

    def build_service_name(self, service_id: str) -> str:
        return f"{self.project_id}-{self.stage}-{service_id}"
