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

	docker run -p 8080:8080 \
        -e CSRF_ENABLED='true' \
        -e DEFAULT_LANGUAGE='fr' \
        sboursault/simple-commerce:2.0

### Build and push the docker image

    docker build -t sboursault/simple-commerce:2.0 --rm=true --no-cache=true .
    docker push sboursault/simple-commerce:2.0

Now the image url is 'docker.io/sboursault/simple-commerce:2.0'.
    
### Admin user

username: superuser
email: superuser@example.com
password: testing
