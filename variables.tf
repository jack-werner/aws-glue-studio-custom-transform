variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "AWS_ACCOUNT_ID" {
  description = "AWS Account id"
  sensitive = true
}