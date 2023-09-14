# eoapi-template

Demonstration application showing the use and configuration options of the [eoapi-cdk constructs](https://github.com/developmentseed/eoapi-cdk) on AWS.

## Requirements

- python
- docker
- the AWS CDK CLI
- AWS credentials environment variables configured to point to an account. 
- **Optional** a `config.yaml` file to override the default deployment settings defined in `config.py`.

## Installation

```
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Deployment

First, synthesize the app 

```
cdk synth --all
```

Then, deploy

```
cdk deploy --all --require-approval never
```