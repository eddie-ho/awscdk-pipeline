#!/usr/bin/env python3

from aws_cdk import core

from pipelines_webinar.pipeline_stack import PipelineStack

PIPELINE_ACCOUNT = '323040907683'

app = core.App()
PipelineStack(app, 'PipelineStack', env={
  'account': PIPELINE_ACCOUNT,
  'region': 'eu-west-2',
})

app.synth()
