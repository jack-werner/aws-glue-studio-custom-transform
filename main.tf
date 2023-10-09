provider "aws" {
    region = var.region
    access_key = var.AWS_ACCESS_KEY
    secret_key = var.AWS_SECRET_KEY
}

resource "aws_s3_object" "object" {
    bucket = var.s3_bucket
    key = "target/example.json"
    source = "transforms/case_transform/case_transform.json"

    etag = filemd5("transforms/case_transform/case_transform.json")
}