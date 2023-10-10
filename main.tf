provider "aws" {
  region = var.region
}

module "custom_glue_studio_case_transform" {
  source     = "./tf_modules/custom_glue_studio_transform/"
  region     = "us-east-1"
  account_id = var.AWS_ACCOUNT_ID
  filename   = "case_transform_2"
  local_path = "transforms/case_transform"
}

# resource "aws_s3_object" "object" {
#   bucket = "aws-glue-assets-${var.AWS_ACCOUNT_ID}-${var.region}"
#   key = "transforms/target/example.json"
#   source = "transforms/case_transform/case_transform_2.json"

#   etag = filemd5("transforms/case_transform/case_transform_2.json")
# }