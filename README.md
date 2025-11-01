# eoapi-template

Template repository to deploy [eoapi](https://eoapi.dev) on AWS using the [eoapi-cdk constructs](https://github.com/developmentseed/eoapi-cdk) or locally with Docker.

## Requirements

- python >=3.9
- docker
- node >=18
- AWS credentials environment variables configured to point to an account.
- **Optional** a `config.yaml` file to override the default deployment settings defined in `config.py`.

## Installation

Install python dependencies with `uv`

```bash
uv sync
```

And node dependencies with

```bash
npm install
```

Verify that the `cdk` CLI is available. Since `aws-cdk` is installed as a local dependency, you can use the `npx` node package runner tool, that comes with `npm`.

```bash
npx cdk --version
```

## Deployment

### Configuration

You can configure your eoAPI deployment using either environment variables (defined manually or in a `.env` file) or a configuration yaml file (see [config.py](./infrastructure/config.py) for more details on all of the configurable parameters.

Feel free to add or subtract from these configuration parameters to suit your needs!

To start you can copy [config.yaml.example](./config.yaml.example) to config.yaml:

```bash
cp config.yaml.example config.yaml
```

Then update the values according to your preferences.
Be sure to set `project_id` to something recognizable and to look closely at all of the components that you are including with each setting.

### AWS credentials

For the deployment steps to work, you will need to have your environment configured with your AWS account credentials.
There are lots of ways to do this so choose whatever method you want to define `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, dtc.

### Synthesize the CDK Stack

You can test your deployment configuration without deploying any actual resources to AWS by using the `cdk synth` command.

```bash
uv run npx cdk synth --all
```

Then, deploy

```bash
uv run npx cdk deploy --all --require-approval never
```

## Docker

Before deploying the application on the cloud, you can start by exploring it with a local *Docker* deployment

```bash
docker compose up
```

Once the applications are *up*, you'll need to add STAC **Collections** and **Items** to the PgSTAC database. If you don't have, you can use the follow the [MAXAR open data demo](https://github.com/vincentsarago/MAXAR_opendata_to_pgstac) (or get inspired by the other [demos](https://github.com/developmentseed/eoAPI/tree/main/demo)).

Then you can start exploring your dataset with:

- the STAC Metadata service [http://localhost:8081](http://localhost:8081)
- the Raster service [http://localhost:8082](http://localhost:8082)
- the Vector service [http://localhost:8083](http://localhost:8083)
- the browser UI [http://localhost:8085](http://localhost:8085)

If you've added a vector dataset to the `public` schema in the Postgres database, they will be available through the **Vector** service at [http://localhost:8083](http://localhost:8083).
