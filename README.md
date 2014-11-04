blackbird-Kinesis
=================

Get Kinesis Stream metrics by using CloudWatch API.


Getting metrics
---------------

This plugin get below metrics.
And this plugin is to observe Kinesis Stream not each shard.
For example, this plugin doesn't get `KinesisDataFetcher.Time`.

### CloudWatch metrics

| CloudWatch metric name             | unit         | blackbird item key                                                   |
|------------------------------------|--------------|----------------------------------------------------------------------|
| PutRecord.Bytes                    | Bytes        | cloudwatch.kinesis.stream.PutRecord.Bytes.Sum                        |
| PutRecord.Latency                  | milliseconds | cloudwatch.kinesis.stream.PutRecord.Latency.Average                  |
| PutRecord.Success                  | Count        | cloudwatch.kinesis.stream.PutRecord.Success.Sum                      |
| GetRecords.Bytes                   | Bytes        | cloudwatch.kinesis.stream.GetRecords.Bytes.Sum                       |
| GetRecords.IteratorAgeMilliseconds | milliseconds | cloudwatch.kinesis.stream.GetRecords.IteratorAgeMilliseconds.Average |
| GetRecords.Latency                 | milliseconds | cloudwatch.kinesis.stream.GetRecords.Latency.Average                 |
| GetRecords.Success                 | Count        | cloudwatch.kinesis.stream.GetRecords.Success.Sum                     |

### Values for per Second

Following values are for per second.

| calculation formula                 | blackbird item key                                    |
|-------------------------------------|-------------------------------------------------------|
| PutRecord.Bytes / getting period    | cloudwatch.kinesis.stream.PutRecordBytes.PerSecond    |
| PutRecord.Success / getting period  | cloudwatch.kinesis.stream.PutRecordSuccess.PerSecond  |
| GetRecords.Bytes / getting period   | cloudwatch.kinesis.stream.GetRecordsBytes.PerSecond   |
| GetRecords.Success / getting period | cloudwatch.kinesis.stream.GetRecordsSuccess.PerSecond |

In other words *getting period* is a value what is written as `interval` in your configuration file.


Configuration file
------------------

See the below settings.

```ini
# You can specify section name anything you like.
[ANYTHING OK]
region_name = us-east-1
aws_access_key_id = YOUR_AWS_ACCESS_KEY_ID
aws_secret_access_key = YOUR_AWS_SECRET_ACCESS_KEY
stream_name = YOUR_STREAM_NAME
hostname = HOSTNAME_ON_ZABBIX_SERVER
```

### region_name

AWS region name.
Default value is us-east-1.
This value is not required.

### aws_access_key_id

AWS Access Key ID.
This value is required.

### aws_secret_access_key

AWS Secret Access Key.
This value is required.

### stream_name

Your Kinesis Stream name.
This value is required.

### hostname

hostname on Zabbix server.
