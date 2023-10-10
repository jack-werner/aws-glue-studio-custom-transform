provider "aws" {
  region = var.region
}

data "aws_kms_key" "this" {
  key_id = var.kms_key_alias
}

resource "aws_s3_object" "json" {
  bucket = "aws-glue-assets-${var.account_id}-${var.region}/transforms"
  key    = "${var.filename}.json"
  source = "${var.local_path}/${var.filename}.json"
  kms_key_id = aws_kms_key.this.arn

  etag = filemd5("${var.local_path}/${var.filename}.json")
}

resource "aws_s3_object" "python" {
  bucket = "aws-glue-assets-${var.account_id}-${var.region}/transforms"
  key    = "${var.filename}.py"
  source = "${var.local_path}/${var.filename}.py"
  kms_key_id = aws_kms_key.this.arn

  etag = filemd5("${var.local_path}/${var.filename}.py")
}