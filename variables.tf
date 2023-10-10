variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "account_id" {
  description = "AWS Account id"
  sensitive = true
}