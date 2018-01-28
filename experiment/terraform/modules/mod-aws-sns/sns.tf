resource "aws_sns_topic" "aws_sns" {
  name = "${var.product}-${var.name}-${var.env}-${var.region}"
}