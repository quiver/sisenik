import time
import boto3
import click
 
@click.command()
@click.option('--stream-name')
@click.option('--shard-iterator-type', default='LATEST')
@click.option('--limit', default=100, type=int, help='record limit size. defaults to 100')
@click.option('--interval', default=10, type=int, help='polling interval in seconds. defaults to 10')
def cli(stream_name, shard_iterator_type, limit, interval):
    '''"tail -f" for AWS Kinesis Streams.
    
    You can pass AWS profile information via environment variables :

    $ AWS_PROFILE=profile sisenik [OPTIONS] 
    '''
    client = boto3.client('kinesis')
    iterators = {}
    shards = client.describe_stream(StreamName = stream_name)['StreamDescription']['Shards']
    for shard in shards:
        response = client.get_shard_iterator(
            StreamName=stream_name,
            ShardId=shard['ShardId'],
            ShardIteratorType=shard_iterator_type
        )
        shard_iterator = response.get('ShardIterator', None)
        if shard_iterator:
            iterators[shard['ShardId']] = shard_iterator
    
    while True:
        for shard, iterator in iterators.items():
            response = client.get_records(
              ShardIterator=iterator,
              Limit=limit
              )
            shard_iterator = response.get('NextShardIterator', None)
            if shard_iterator:
                iterators[shard] = shard_iterator
            else:
                iterators.pop(shard)
            for record in response['Records']:
                click.echo(record['Data'])
        time.sleep(interval)
