variable "region" {
  description = "The AWS region to deploy to"
  type        = string
}

variable "account_id" {
  description = "Your AWS account id"
  type        = string
  sensitive   = true
}

variable "filename" {
  description = "The name of your json and python files. Do not include filetype extensions."
  type        = string
}

variable "local_path" {
  description = "The local path to your json and python files. Do not include trailing slash."
  type        = string
}

variable "kms_key_alias" {
  description = "The KMS key alias used to encrypt the S3 bucket"
  type        = string
  default     = "aws/s3"
}