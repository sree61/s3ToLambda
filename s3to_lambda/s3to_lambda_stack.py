from aws_cdk import (
    core,
    aws_s3 as _s3,
    aws_sns as _sns,
    aws_sns_subscriptions as _sns_subscriptions,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _event,
    )


class S3ToLambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_s3_bucket = _s3.Bucket(
            self,
            id = 'myS3Bucket'
        )

        my_sns_topic = _sns.Topic(\
            self, 
            id = 'demoTopic'
        )

        my_sns_sub = _sns_subscriptions.EmailSubscription("sreeamaravila@gmail.com")
        my_sns_sub.bind(my_sns_topic)

        my_function = _lambda.Function(
            self,
            id = 'demoFunction',
            code = _lambda.Code.asset(r'../src'),
            handler = 'fun01.handler'
            )
        trigger_event = _event.S3EventSource(
            bucket = my_s3_bucket,
            events = [_s3.EventType.OBJECT_CREATED]
        )
