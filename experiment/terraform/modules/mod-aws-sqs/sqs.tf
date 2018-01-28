resource "aws_sqs_queue" "aws_sqs" {
  name                      = "${var.product}-${var.name}-${var.env}-${var.region}"
  message_retention_seconds = 86400

  tags {
    Product = "${var.product}"
    Name = "${var.product}-${var.name}-${var.env}-${var.region}"
    Component = "${var.component}"
    Env = "${var.env}"
    Region = "${var.region}"
  }
}