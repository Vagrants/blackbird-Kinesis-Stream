#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import logging

import moto
import nose.tools

import kinesis_stream


class TestFetchMetricsSuite(object):

    def __init__(self):
        options = {
            'region_name': 'us-east-1',
            'aws_access_key_id': 'NONE',
            'aws_secret_access_key': 'NONE',
            'stream_name': 'TESTING_STREAM',
            'interval': 300
        }
        self.concrete_job = kinesis_stream.ConcreteJob(
            options=options,
            logger=logging
        )

        self.checking_keys = list()
        self.checking_keys.extend(
            [x.keys()[0] for x in self.concrete_job.metrics_config]
        )
        self.checking_keys.extend(
            self.concrete_job.per_second_key_mapping.keys()
        )

    def test_fetch_metrics(self):
        raise NotImplementedError(
            'Sorry! moto v0.3.8 not implement mock_cloud_watch. '
            'When it\'s implemented, we write this test.'
        )
