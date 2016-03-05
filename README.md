# sisenik
"tail -f" for AWS Kinesis Streams

## Install

```
$ pip install sisenik
```

## Usage

```
$ sisenik --stream-name foo
$ AWS_PROFILE=dev sisenik --stream-name test-stream --shard-iterator-type TRIM_HORIZON
```

## Development

First create a new virtual environment

```
$ virtualenv venv
$ . venv/bin/activate
```

Clone a sisenik repository and install it locally.

```
$ git clone https://github.com/quiver/sisenik.git
$ cd sisenik
$ pip install --editable .
```

Run it

```
$ sisenik --help
Usage: sisenik [OPTIONS]

  "tail -f" for AWS Kinesis Streams.

  You can pass AWS profile information via environment variables :

  $ AWS_PROFILE=profile sisenik [OPTIONS]

Options:
  --stream-name TEXT
  --shard-iterator-type TEXT
  --limit INTEGER             record limit size. defaults to 100
  --interval INTEGER          polling interval in seconds. defaults to 10
  --help                      Show this message and exit.
```
