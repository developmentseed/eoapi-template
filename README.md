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

## GitHub Actions

The repository includes a CI workflow (`.github/workflows/ci.yml`) that runs on every push to `main` and on all pull requests. The workflow:

1. Sets up the build environment with Node.js 22 and Python (via `uv`)
2. Installs all project dependencies (both Python and Node)
3. Runs pre-commit hooks to check code quality and formatting
4. Synthesizes the CDK stack to validate the infrastructure-as-code configuration

This ensures that all code changes pass quality checks and that the CDK stack can be successfully synthesized before merging.

### Automated Deployment

The workflow also includes an example `deploy` job that demonstrates how to automatically deploy your eoAPI stack to AWS using GitHub Actions. This job showcases:

- **AWS OIDC authentication** - Secure, keyless authentication using GitHub's OIDC provider
- **GitHub Environments** - Pulling deployment configuration from environment-specific variables
- **Protection rules** - Leveraging GitHub's environment protection features (approvals, branch restrictions)

> [!NOTE]
> This deployment job is a basic starting point and can be triggered manually via `workflow_dispatch`. You should tailor it to match your specific deployment strategy, such as:
>
> - Adding multiple environments (staging, production, etc.)
> - Implementing deployment approval workflows
> - Adding post-deployment validation or smoke tests
> - Customizing environment variables for different stages
> - Integrating with monitoring or notification systems

To set up AWS OIDC authentication for GitHub Actions, refer to the [AWS documentation on configuring OIDC with GitHub](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) and the [GitHub documentation for Configuring OpenID Connect in AWS](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws).

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
