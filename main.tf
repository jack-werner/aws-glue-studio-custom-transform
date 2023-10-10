provider "aws" {
  region = var.region
}

module "custom_glue_studio_case_transform" {
  source = "tf_modules/custom_glue_studio_transform/"
  region = "us-east-1"
  account_id = var.account_id
  file_name = "case_transform_2"
  local_path = "transforms/case_transform"
}