variable "AWS_ACCESS_KEY_ID" {
  description = "AWS Access Key ID"
  type = string
  sensitive = true
}

variable "AWS_SECRET_ACCESS_KEY" {
  description = "AWS Secret Access Key"
  type = string
  sensitive = true
}

variable "region" {
  description = "AWS region"
  default = "us-east-1"
}

variable "s3_bucket" {
  description = "s3 bucket to upload your file to"
}