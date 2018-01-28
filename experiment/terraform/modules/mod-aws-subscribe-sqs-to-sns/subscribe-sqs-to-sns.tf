data "aws_iam_policy_document" "sns_topic_policy" {
  policy_id = "allow_sqs_to_subscribe_to_sns"

  statement {
    actions = [
      "SNS:Subscribe",
      "SNS:Receive",
    ]

    condition {
      test     = "StringLike"
      variable = "SNS:Endpoint"

      values = [
        "${var.queue_id["arn"]}"
      ]
    }

    effect = "Allow"

    principals {
      type        = "AWS"
      identifiers = ["*"]
    }

    resources = [
      "${var.notifier_id}",
    ]

    sid = "__console_sub_0"
  }
}

data "aws_iam_policy_document" "sqs_queue_policy" {
  policy_id = "${var.queue_id["arn"]}/SQSDefaultPolicy"

  statement {
    sid    = "sns-topic"
    effect = "Allow"

    principals {
      type        = "AWS"
      identifiers = ["*"]
    }

    actions = [
      "SQS:SendMessage"
    ]

    resources = [
      "${var.queue_id["arn"]}"
    ]

    condition {
      test     = "ArnEquals"
      variable = "aws:SourceArn"

      values = [
        "${var.notifier_id}",
      ]
    }
  }
}

resource "aws_sqs_queue_policy" "sqs_queue_policy" {
  queue_url = "${var.queue_id["url"]}"

  policy = "${data.aws_iam_policy_document.sqs_queue_policy.json}"
}

resource "aws_sns_topic_policy" "sns_topic_policy" {
  arn = "${var.notifier_id}"
  policy = "${data.aws_iam_policy_document.sns_topic_policy.json}"
}

resource "aws_sns_topic_subscription" "subscribe_sqs_to_sns" {
  topic_arn = "${var.notifier_id}"
  protocol = "sqs"
  endpoint = "${var.queue_id["arn"]}"
}