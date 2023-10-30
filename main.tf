provider "aws" {
  region = var.region
}

module "custom_glue_studio_case_transform" {
  source     = "./tf_modules/custom_glue_studio_transform/"
  region     = "us-east-1"
  account_id = var.AWS_ACCOUNT_ID
  filename   = "case_transform_string"
  local_path = "transforms/case_transform"
}