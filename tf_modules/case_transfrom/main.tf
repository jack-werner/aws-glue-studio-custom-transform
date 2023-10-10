provider "aws" {
  region = var.region
}

resource "aws_s3_object" "json" {
  bucket = "aws-glue-assets-${var.account_id}-${var.region}/transforms"
  key = "${var.filename}.json"
  source = "${var.source}/${var.filename}.json"

  etag = filemd5("${var.source}/${var.filename}.json")
}

resource "aws_s3_object" "python" {
  bucket = "aws-glue-assets-${var.account_id}-${var.region}/transforms"
  key = "${var.filename}.py"
  source = "${var.source}/${var.filename}.py"

  etag = filemd5("${var.source}/${var.filename}.py")
}