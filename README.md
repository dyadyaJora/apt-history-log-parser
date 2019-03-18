# Task

## How to run

Build

    docker build -t tt-aio .

Run

    docker run -p 8080:8080 -t tt-aio
    
## How to test

- Open `0.0.0.0:8080/last-upgrade`
  - Error no info
- Run `docker exec [id] bash -c 'apt-get upgrade -y'`
- Open `0.0.0.0:8080/last-upgrade`
  - Checking timestamp