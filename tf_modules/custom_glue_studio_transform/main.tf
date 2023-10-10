provider "aws" {
  region = var.region
}

resource "aws_s3_object" "json" {
  bucket = "aws-glue-assets-${var.account_id}-${var.region}/transforms"
  key    = "${var.filename}.json"
  source = "${var.local_path}/${var.filename}.json"
  server_side_encryption = "aws:kms"

  # etag = filemd5("${var.local_path}/${var.filename}.json")
}

resource "aws_s3_object" "python" {
  bucket = "aws-glue-assets-${var.account_id}-${var.region}/transforms"
  key    = "${var.filename}.py"
  source = "${var.local_path}/${var.filename}.py"
  server_side_encryption = "aws:kms"

  # etag = filemd5("${var.local_path}/${var.filename}.py")
}