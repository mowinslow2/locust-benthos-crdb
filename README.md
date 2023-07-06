# locust-benthos-crdb
Using Locust (testing framework) to POST messages to Benthos (stream processing) and Insert into CockroachDB. 

Blog with more detailed instructions and writeup can be found [here](https://morgans-blog.deno.dev/locust-benthos-cockroachdb). 

## CockroachDB

Create the following table

```
CREATE TABLE tracking (
    id UUID PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
    ride_id UUID NOT NULL,
    latitude FLOAT8 NOT NULL,
    longitude FLOAT8 NOT NULL,
    tracking_point GEOGRAPHY(POINT,4326) NULL,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);
```

## Benthos

### Install

```
curl -Lsf https://sh.benthos.dev | bash
```

### Create Config

Create base config with the following command, or use the config.yaml in this repo. 

```
benthos create > config.yaml
```

### Run

benthos -c ./config.yaml

## Locust

### Install

Need python installed beforehand. 

```
pip3 install locust
```

### Run

**Single**

```
$ locust
```

**Multiple Workers**

```
$ locust --master
```

```
$ locust --worker
```