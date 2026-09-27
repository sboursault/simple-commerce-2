# Simple-commerce

## How to run simple-commerce

### From the source code

postgresql must be installed on the machine
    
    virtualenv --python=python3 venv  
    source ./venv/bin/activate
    make sandbox
    sandbox/manage.py runserver

(source: https://docs.oscarcommerce.com/en/latest/internals/sandbox.html)

### Using the docker image

    # run with embedded sqlite db
	docker run \ 
        -p 8080:8080 \
        -e CSRF_ENABLED='true' \
        -e DEFAULT_LANGUAGE='fr' \
        sboursault/simple-commerce:2.4-dev-slim

    # init pg db
	docker run \
        --env-file .env.scw \
        sboursault/simple-commerce:2.4-dev make build_sandbox

    # run with pg db
	docker run \
        --env-file .env.scw \
        sboursault/simple-commerce:2.4-dev-slim


### Build and push the docker image

    docker build --build-arg BASE_IMAGE=python:3.12 -t sboursault/simple-commerce:2.4-dev --rm=true --no-cache=true -f Dockerfile-dev .
    docker push sboursault/simple-commerce:2.4-dev

    docker build --build-arg BASE_IMAGE=python:3.12-slim -t sboursault/simple-commerce:2.4-dev-slim --rm=true --no-cache=true -f Dockerfile-dev .
    docker push sboursault/simple-commerce:2.4-dev-slim

Now the image url is 'docker.io/sboursault/simple-commerce:2.4-dev-slim'.
    
### Admin user

username: superuser
email: superuser@example.com
password: testing


## Scaleway installation steps

Create the database instance `pg-server`. It must have at 100Mb per database/schema.
Create user `simple-commerce`.
Create the database `simple-commerce-<whatever>`
Give permissions to `simple-commerce`
Link the database to the private network `simple-commerce-vpn`

Create the application namespace `simple-commerce-staging`.
Deploy the container `<whatever>`, based on `docker.io/sboursault/simple-commerce:2.4-dev-slim`
- Port `8080`,
- Resource `2000 mVCPU`, Mémoire `4096 Mo`
- Instances min : 0, Instance max 1
Link the container to the private network.
- tip : most variables can be specified at the name-space level.
