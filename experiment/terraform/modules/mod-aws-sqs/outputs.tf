output "id" {
  value = {
    arn = "${aws_sqs_queue.aws_sqs.arn}"
    url = "${aws_sqs_queue.aws_sqs.id}"
  }
}
