provider "aws" {
    region = var.region
}

resource "aws_s3_object" "object" {
    bucket = var.s3_bucket
    key = "target/example.json"
    source = "transforms/case_transform/case_transform.json"

    etag = filemd5("transforms/case_transform/case_transform.json")
}