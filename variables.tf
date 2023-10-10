variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "AWS_ACCOUNT_ID" {
  description = "AWS Account id"
  sensitive   = true
}

variable "s3_bucket" {
  description = "the s3bucket to upload to"
  type = string
}